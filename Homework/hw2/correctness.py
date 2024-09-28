from os import urandom
import scheme1,scheme2

def test_correctness():
    """Test the correctness of the encryption and decryption."""
    # Generate a random message of random length. Correctness of an encryption scheme is required for all messages of arbirary length. Here we check correctness on only a random message. 
    message_length = urandom(1)[0]  # Random length between 0 and 255
    message = urandom(message_length)

    # Generate key
    key = scheme1.keygen()

    # Encrypt the message
    ciphertext = scheme1.enc(key, message)

    # Decrypt the message
    decrypted_message = scheme2.dec(key, ciphertext)

    # Check if the decrypted message matches the original message
    assert message == decrypted_message, "Decryption failed: Original and decrypted messages do not match"

    return "Test passed: Encryption and decryption are correct"    

### RUNNING THE TESTS ###

# Correctness tests: Ensure the encryption and decryption functions successfully work
print("\n========== CORRECTNESS TEST ==========\n")
print(test_correctness())

