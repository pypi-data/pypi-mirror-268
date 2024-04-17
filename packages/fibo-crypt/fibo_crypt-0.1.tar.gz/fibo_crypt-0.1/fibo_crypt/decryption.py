from .encryption import fibonacci_mod

def decrypt_string(s, key):
    fib_sequence = fibonacci_mod(len(s), key)
    altered_chars = list(s)
    for i in reversed(range(len(s))):
        move = fib_sequence[i]
        if i + move < len(s):
            altered_chars[i], altered_chars[(i + move) % len(s)] = altered_chars[(i + move) % len(s)], altered_chars[i]
        altered_chars[i] = chr((ord(altered_chars[i]) - key) % 128)
    return ''.join(altered_chars)