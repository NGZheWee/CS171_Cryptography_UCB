import random, scheme1, adversary
# Observe that security definition does not use scheme2.decrypt. 

def security():
    """Security function that evaluates the adversary."""
    # Adversary specifies two messages
    m0, m1 = adversary.adversary(1)
    
    # Check that the lengths of the messages are the same
    if len(m0) != len(m1):
        raise ValueError("The lengths of the two messages must be the same")
    
    # Encrypt a random one of the messages
    b = random.choice([0, 1])
    if b == 0:
        chosen_message  = m0
    else:
        chosen_message = m1
    key = scheme1.keygen() # Generate a key
    ciphertext = scheme1.enc(key, chosen_message)

    # Adversary tries to guess which message was encrypted
    bprime = adversary.adversary(2, ciphertext)

    # Determine if the adversary's guess is correct
    return 1 if bprime == b else 0

        
### RUNNING THE TESTS ###

# Adversary tests: Ensure the code can uncover the key
print("\n========== ATTACK TEST ==========\n")
# Test the security function with both adversaries
def run_security_test(num_iterations):
    """Runs the security function a specified number of times and checks if it always returns 1."""
    """In the security definition breaking the scheme with probability non-negligibly better than 1/2 suffice. However, here we ask that the adversary succeed with probability 1."""
    for _ in range(num_iterations):
        if security() != 1:
            print("Test failed: security function returned 0")
            return
    print("Test passed: security function always returned 1")
run_security_test(1000)
