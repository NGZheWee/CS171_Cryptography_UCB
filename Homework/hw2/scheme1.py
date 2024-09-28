from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def keygen():
    # Generate key
    key = os.urandom(32)
    
    return key

def enc(key, plaintext):
    """Encrypt the plaintext message using the given encryption scheme."""
    # Initialize AES cipher with key and a zero IV
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the zero value
    zero_value_encrypted = encryptor.update(b'\x00' * 16) + encryptor.finalize()

    # XOR the plaintext with the encrypted zero value
    aes_ciphertext = bytes([m ^ z for m, z in zip(plaintext, zero_value_encrypted * (len(plaintext) // 16 + 1))])

    # In order to be sure that encryption/decryption is working the programmer includes additional
    # information in the ciphertext. Specifically, compute the XOR of all bytes in the plaintext
    xor_all_bytes = 0
    for byte in plaintext:
        xor_all_bytes ^= byte
    
    return aes_ciphertext, xor_all_bytes
