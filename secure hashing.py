# SHA-256 example
def rr(word, count):
    # Right-rotate bits in a 32-bit word
    return ((word >> count) | (word << (32 - count))) % 2**32