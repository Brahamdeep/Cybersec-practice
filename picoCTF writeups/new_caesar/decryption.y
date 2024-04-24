import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(enc):
    dec = ""
    for i in range(0, len(enc), 2):
        pair = enc[i:i+2]
        binary = "{:04b}{:04b}".format(ALPHABET.index(pair[0]), ALPHABET.index(pair[1]))
        dec += chr(int(binary, 2))
    return dec

def reverse_shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

encrypted_message = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"
key = "g"

decrypted_b16 = ""
for i, c in enumerate(encrypted_message):
    decrypted_b16 += reverse_shift(c, key[i % len(key)])

decrypted_message = b16_decode(decrypted_b16)
print(decrypted_message)
