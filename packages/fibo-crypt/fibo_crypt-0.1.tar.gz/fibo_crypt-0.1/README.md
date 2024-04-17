# fibo_crypt

fibo_crypt is a Python package that provides encryption and decryption functionality using the Fibonacci sequence.

## Installation

You can install fibo_crypt from PyPI using pip:

`pip install fibo_crypt`
## Usage

Here's an example of how to use the package:

```python
import fibo_crypt

# Generate a key
key = fibo_crypt.generate_key()

# Encrypt a string
plaintext = "Hello, World!"
ciphertext = fibo_crypt.encrypt_string(plaintext, key)
print(f"Encrypted text: {ciphertext}")

# Decrypt the ciphertext
decrypted_text = fibo_crypt.decrypt_string(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")