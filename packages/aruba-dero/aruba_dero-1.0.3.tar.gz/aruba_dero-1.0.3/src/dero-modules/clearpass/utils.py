import tempfile

from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.dh import DHPrivateKey
from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.x448 import X448PrivateKey
from cryptography.hazmat.primitives.serialization import BestAvailableEncryption
from cryptography.hazmat.primitives.serialization import pkcs12, load_pem_private_key, load_der_private_key
from cryptography.x509 import Certificate


def check_cert_and_convert_to_pem(filename: str) -> tuple[str | None, Certificate | None]:
    with open(filename, 'rb') as file:
        cert_data = file.read()
        if not cert_data:
            return None, None

    try:
        # Try to load as PEM
        cert = x509.load_pem_x509_certificate(cert_data)
    except ValueError:
        try:
            # If loading as PEM fails, try to load as DER
            cert = x509.load_der_x509_certificate(cert_data)
        except ValueError:
            # If both checks fail, return None
            return None, None

    # Output as PEM
    return write_public_to_pem(cert)


def check_key_and_convert_to_pem(filename: str, passphrase=None) -> tuple[
    str | None, DHPrivateKey | Ed25519PrivateKey | Ed448PrivateKey | RSAPrivateKey | DSAPrivateKey | EllipticCurvePrivateKey | X25519PrivateKey | X448PrivateKey | None]:
    with open(filename, 'rb') as file:
        key_data = file.read()
        if not key_data:
            return None, None

        passphrase = passphrase.encode() if passphrase else None

        try:
            # Try to load as PEM
            key = load_pem_private_key(key_data, passphrase)
        except ValueError:
            try:
                # If loading as PEM fails, try to load as DER
                key = load_der_private_key(key_data, passphrase)
            except ValueError:
                # If both checks fail, return None
                return None, None
        return write_private_to_pem(key, passphrase)


def pkcs12_to_pem(filename: str, passphrase: str) -> tuple[str | None, object | None]:
    with open(filename, 'rb') as file:
        cert_data = file.read()
        if not cert_data:
            return None, None
    try:
        p12 = pkcs12.load_key_and_certificates(data=cert_data, password=passphrase.encode())
        cert = p12[1]

        if cert is None:
            return None, None
        return write_public_to_pem(cert)
    except ValueError:
        return None, None


def write_public_to_pem(cert) -> tuple[str, Certificate]:
    pem_data = cert.public_bytes(serialization.Encoding.PEM)

    # Write the PEM data to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(pem_data)
    temp_file.close()

    return temp_file.name, cert


def write_private_to_pem(
        key: DHPrivateKey | Ed25519PrivateKey | Ed448PrivateKey | RSAPrivateKey | DSAPrivateKey | EllipticCurvePrivateKey | X25519PrivateKey | X448PrivateKey | None,
        passphrase: str | None) -> tuple[
    str, DHPrivateKey | Ed25519PrivateKey | Ed448PrivateKey | RSAPrivateKey | DSAPrivateKey | EllipticCurvePrivateKey | X25519PrivateKey | X448PrivateKey | None]:
    pem_data = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption() if passphrase is None else BestAvailableEncryption(passphrase.encode())
    )

    # Write the PEM data to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(pem_data)
    temp_file.close()

    return temp_file.name, key


def bundle_pkcs12(cert: Certificate,
                  key: DHPrivateKey | Ed25519PrivateKey | Ed448PrivateKey | RSAPrivateKey | DSAPrivateKey | EllipticCurvePrivateKey | X25519PrivateKey | X448PrivateKey | None,
                  passphrase=None) -> tuple[str | None, bytes | None]:
    p12 = pkcs12.serialize_key_and_certificates(
        f"{cert.subject}".encode(), key, cert, None, BestAvailableEncryption(f"{passphrase}".encode())
    )

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(p12)
    temp_file.close()
    return temp_file.name, p12
