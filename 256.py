## Secure Hasing Algorithm 256
def rr(word, count):
    # Right-rotate bits in a 32-bit word
    return ((word >> count) | (word << (32 - count))) % 2 ** 32


def ch(e, f, g):
    # Choice function combines 5th, 6th, and 7th words for algorithm
    return (e & f) ^ ((~e) & g)


def maj(a, b, c):
    # Majority function combines 1st, 2nd, and 3rd words for algorithm
    return (a & b) ^ (a & c) ^ (b & c)


def s0(word):
    # Sigma σ0 function for creating word list
    return rr(word, 7) ^ rr(word, 18) ^ (word >> 3)


def s1(word):
    # Sigma σ1 function for creating word list
    return rr(word, 17) ^ rr(word, 19) ^ (word >> 10)


def S0(word):
    # Sigma Σ0 function for compression phase
    return rr(word, 2) ^ rr(word, 13) ^ rr(word, 22)


def S1(word):
    # Sigma Σ1 function for compression phase
    return rr(word, 6) ^ rr(word, 11) ^ rr(word, 25)


def pad_message(message):
    # Pre-process message for use as bytes
    # Find message length in bits. Assume each character in the message is 1 byte (8 bits)
    L = len(message) * 8
    # Change the message into a series of bytes
    message_int = 0
    for c in range(len(message)):
        message_int = message_int << 8
        message_int += ord(message[c])
    # Append a 1 bit to the right of the message
    message_int = (message_int << 1) + 1
    # Append filler zeroes so that L + 1 bit + 64 = a multiple of 512
    filler_zeroes = 512 - ((L + 65) % 512)
    message_int = message_int << filler_zeroes
    # Append the message length as a 64-bit number
    message_int = (message_int << 64) + L
    return message_int


def SHA256(message: int):
    # SHA-256 process using preprocessed message
    # Initial hash values
    hash_list = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    # Round constants
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xb378d6fddddd, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]
    # Iterate through each chunk
    chunk_count = (message.bit_length() - 1) // 512 + 1
    for i in range(chunk_count):
        # Set the chunk and create the first 16 words for the word schedule
        chunk = (message >> (512 * (chunk_count - 1 - i))) % 2 ** 512
        word_array = []
        for w in range(16):
            word = (chunk >> (32 * (15 - w))) % 2 ** 32
            word_array.append(word)
        # Extend the word schedule using the σ functions
        for w in range(16, 64):
            word = (word_array[w - 16] + word_array[w - 7] + s0(word_array[w - 15]) + s1(word_array[w - 2])) % 2 ** 32
            word_array.append(word)
        # Start the temporary hash values using the initial hash list. It breaks if you just set temp_hash = hash_list
        temp_hash = [0 for _ in range(8)]
        for h in range(8):
            temp_hash[h] = hash_list[h]
        # Iterate through every word in the word schedule
        for w in range(64):
            t1 = (k[w] + word_array[w] + ch(temp_hash[4], temp_hash[5], temp_hash[6])
                  + S1(temp_hash[4]) + temp_hash[7]) % 2 ** 32
            t2 = (S0(temp_hash[0]) + maj(temp_hash[0], temp_hash[1], temp_hash[2])) % 2 ** 32
            # Update the temporary values
            temp_hash[7] = temp_hash[6]
            temp_hash[6] = temp_hash[5]
            temp_hash[5] = temp_hash[4]
            temp_hash[4] = (temp_hash[3] + t1) % 2 ** 32
            temp_hash[3] = temp_hash[2]
            temp_hash[2] = temp_hash[1]
            temp_hash[1] = temp_hash[0]
            temp_hash[0] = (t1 + t2) % 2 ** 32
        # Set the hash list using the final temporary values
        for h in range(8):
            hash_list[h] = (hash_list[h] + temp_hash[h]) % 2 ** 32
    # Create the hash digest by grouping hash words together
    digest = 0
    for h in range(8):
        digest = digest << 32
        digest = digest + hash_list[h]
    return digest


# Test SHA-256 using an empty string and a very long string (> 512 bits)
# You can compare them at https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values
m1 = ""
p1 = pad_message(m1)
h1 = SHA256(p1)
print(hex(p1))
print(hex(h1))
m2 = "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"
p2 = pad_message(m2)
h2 = SHA256(p2)
print(hex(h2))