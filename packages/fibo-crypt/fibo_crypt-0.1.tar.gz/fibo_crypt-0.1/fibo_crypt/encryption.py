def fibonacci_mod(n, key):
    l = []
    a, b = 0, 1
    for i in range(n):
        l.append(b)
        a, b = b, a + b
    return [(x % key) if (x % key) % 2 == 0 else -(x % key) for x in l]

def encrypt_string(s, key):
    fib_sequence = fibonacci_mod(len(s), key)
    altered_chars = list(s)
    for i, move in enumerate(fib_sequence):
        altered_chars[i] = chr((ord(altered_chars[i]) + key) % 128)
        if i + move < len(s):
            altered_chars[i], altered_chars[(i + move) % len(s)] = altered_chars[(i + move) % len(s)], altered_chars[i]
    return ''.join(altered_chars)