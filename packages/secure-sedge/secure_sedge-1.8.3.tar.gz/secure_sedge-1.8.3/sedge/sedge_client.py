from io import StringIO
from collections import defaultdict
import json
import binascii
import cryptography.hazmat.backends
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from OpenSSL.crypto import X509Req, load_privatekey, X509Extension
from OpenSSL.crypto import dump_certificate_request, FILETYPE_ASN1
from OpenSSL.crypto import FILETYPE_PEM
from sewer.client import Client as SewerClient
from sewer.lib import log_response, safe_base64


class SedgeClient(SewerClient):
    """
    overrides serwer.Client to add downloading of the alternate
    cert path chain provided by lets encrypt
    """
    def acme_register(self):
        """
        https://tools.ietf.org/html/draft-ietf-acme-acme#section-7.3
        The server creates an account and stores the public key used to
        verify the JWS (i.e., the 'jwk' element of the JWS header) to
        authenticate future requests from the account.
        The server returns this account object in a 201 (Created) response, with the account URL
        in a Location header field.
        This account URL will be used in subsequest requests to ACME,
        as the 'kid' value in the acme header.
        If the server already has an account registered with the provided
        account key, then it MUST return a response with a 200 (OK) status
        code and provide the URL of that account in the Location header field.
        If there is an existing account with the new key
        provided, then the server SHOULD use status code 409 (Conflict) and
        provide the URL of that account in the Location header field
        """
        self.logger.info(
            'acme_register (%s)',
            'prior registered' if self.PRIOR_REGISTERED else 'new')
        if self.PRIOR_REGISTERED:
            payload = {'onlyReturnExisting': True}
        elif self.contact_email:
            payload = {
                'termsOfServiceAgreed': True,
                'contact': [f'mailto:{self.contact_email}'],
            }
        else:
            payload = {'termsOfServiceAgreed': True}

        url = self.ACME_NEW_ACCOUNT_URL
        acme_register_response = self.make_signed_acme_request(
            url=url, payload=json.dumps(payload), needs_jwk=True
        )
        self.logger.debug(
            'acme_register_response. status_code=%s. response=%s',
            acme_register_response.status_code, log_response(acme_register_response),
        )

        if acme_register_response.status_code not in [201, 200, 409]:
            raise ValueError(
                'Error while registering: '
                f'status_code={acme_register_response.status_code} '
                f'response={log_response(acme_register_response)}')

        kid = acme_register_response.headers['Location']
        setattr(self, 'kid', kid)

        self.logger.info('acme_register_success')
        return acme_register_response

    def download_certificate(self, certificate_url: str) -> str:
        self.logger.info('download_certificate from %s', certificate_url)

        response = self.make_signed_acme_request(certificate_url, payload='')
        self.logger.info('[download cert headers]')
        link = response.headers['link']
        pieces = link.split(', ')
        links = defaultdict(list)
        for x in pieces:
            link, rel = x.split(';', 1)
            link = link[1:-1]
            rel = rel[5:-1]
            links[rel].append(link)
        self.logger.info('links: %s', json.dumps(links, indent=2))
        self.logger.debug(
            'download_certificate_response. status_code={%s}. response={%s}',
            response.status_code, log_response(response)
        )
        if response.status_code not in [200, 201]:
            raise ValueError(
                'Error fetching signed certificate: '
                f'status_code={response.status_code} '
                f'response={log_response(response)}')
        pem_certificate = response.content.decode('utf-8')
        alternates = links.get('alternate') or []
        certs = [ pem_certificate ]
        self.logger.info('download_certificate_success, found %s alternates', len(alternates))
        for url in alternates:
            self.logger.info('downloading alternate cert from %s', url)
            response = self.make_signed_acme_request(url, payload='')
            cert_content = response.text
            self.logger.info('cert content:\n%s', cert_content)
            certs.append(cert_content)
        return certs

    def create_csr(self):
        """
        https://tools.ietf.org/html/draft-ietf-acme-acme#section-7.4
        The CSR is sent in the base64url-encoded version of the DER format. (NB: this
        field uses base64url, and does not include headers, it is different from PEM.)
        """
        self.logger.debug('create_csr')
        req = X509Req()
        req.get_subject().CN = self.domain_name

        sans = [ self.domain_name ]
        if self.domain_alt_names:
            sans += self.domain_alt_names
        sans = [ f'DNS:{x}' for x in sans ]
        san = ', '.join(sans).encode('utf-8')

        req.add_extensions([
            X509Extension(
                'subjectAltName'.encode('utf8'), critical=False, value=san
            )
        ])
        pk = load_privatekey(FILETYPE_PEM, self.certificate_key.encode())
        req.set_pubkey(pk)
        req.set_version(0)
        req.sign(pk, self.digest)
        return dump_certificate_request(FILETYPE_ASN1, req)

    def get_jwk(self):
        """
        calculate the JSON Web Key (jwk) from self.account_key
        """
        private_key = load_pem_private_key(
            self.account_key.encode(),
            password=None,
            backend=default_backend(),
        )
        public_key_public_numbers = private_key.public_key().public_numbers()
        # private key public exponent in hex format
        exponent = f'{public_key_public_numbers.e:x}'
        exponent = f'0{exponent}' if len(exponent) % 2 else exponent
        # private key modulus in hex format
        modulus = f'{public_key_public_numbers.n:x}'
        jwk = {
            'kty': 'RSA',
            'e': safe_base64(binascii.unhexlify(exponent)),
            'n': safe_base64(binascii.unhexlify(modulus)),
        }
        return jwk
