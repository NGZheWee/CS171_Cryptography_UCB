import scheme1

"""
However, the critical piece of information that the adversary exploits is not the AES ciphertext itself but the XOR of 
all bytes in the original plaintext, which is sent along with the AES ciphertext as part of the encryption scheme's 
output.
"""
def adversary(call, encrypted_message=None):
    """Adversary function."""
    if call == 1:
        # First call: Adversary specifies two messages with predictable and distinct XOR results
        # Create two messages with different patterns
        m0 = bytes([0] * 16)  # XOR result will be 0
        m1 = bytes([0] * 15 + [1])  # XOR result will be 1

        return m0, m1
    elif call == 2:
        # Second call: Adversary guesses which message was encrypted based on the XOR value
        # The adversary receives the ciphertext, which includes the XOR of the plaintext bytes
        aes_ciphertext, xor_all_bytes = encrypted_message

        # Guess which message was encrypted based on the XOR value
        # The guess is based on the last byte of the message, as the other bytes are the same
        bprime = 0 if xor_all_bytes == 0 else 1

        return bprime