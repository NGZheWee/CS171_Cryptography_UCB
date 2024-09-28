from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def dec(key, ciphertext_xor_pair):
    """Decrypt the message using the given encryption scheme."""
    # Unpack the ciphertext and the XOR of all bytes
    ciphertext, xor_all_bytes = ciphertext_xor_pair

    # Initialize AES cipher with key and a zero IV
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Decrypt the zero value
    zero_value_encrypted = encryptor.update(b'\x00' * 16) + encryptor.finalize()

    # XOR the ciphertext with the decrypted zero value to get the plaintext
    plaintext = bytes([m ^ z for m, z in zip(ciphertext, zero_value_encrypted * (len(ciphertext) // 16 + 1))])

    # Recalculate the XOR of all bytes in the plaintext
    xor_all_bytes_check = 0
    for byte in plaintext:
        xor_all_bytes_check ^= byte

    # Check if the recalculated XOR matches the received XOR value
    assert xor_all_bytes_check == xor_all_bytes, "Integrity check failed: XOR of all bytes does not match"

    return plaintext