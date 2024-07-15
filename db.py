def initial_permutation(block):
    table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7,
    ]
    return [block[i - 1] for i in table]

def final_permutation(block):
    table = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25,
    ]
    return [block[i - 1] for i in table]

def expand_permutation(block):
    table = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1,
    ]
    return [block[i - 1] for i in table]

def permutation(block, table):
    return [block[i - 1] for i in table]

def sbox_permutation(block):
    sbox = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ],
    ]
    
    result = []
    for i in range(8):
        row = (block[i*6] << 1) + block[i*6+5]
        col = (block[i*6+1] << 3) + (block[i*6+2] << 2) + (block[i*6+3] << 1) + block[i*6+4]
        sbox_value = sbox[i][row][col]
        result.extend([int(b) for b in f"{sbox_value:04b}"])
    
    return result

def permuted_choice_1(key):
    table = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4,
    ]
    return [key[i - 1] for i in table]

def permuted_choice_2(key):
    table = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32,
    ]
    return [key[i - 1] for i in table]

def left_shift(key, shifts):
    return key[shifts:] + key[:shifts]

def generate_keys(initial_key):
    permuted_key = permuted_choice_1(initial_key)
    left_key = permuted_key[:28]
    right_key = permuted_key[28:]
    round_keys = []
    
    for shift in [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]:
        left_key = left_shift(left_key, shift)
        right_key = left_shift(right_key, shift)
        combined_key = left_key + right_key
        round_keys.append(permuted_choice_2(combined_key))
    
    return round_keys

def f_function(right_block, key):
    expanded_block = expand_permutation(right_block)
    xor_block = [b ^ k for b, k in zip(expanded_block, key)]
    sbox_output = sbox_permutation(xor_block)
    final_output = permutation(sbox_output, [
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25,
    ])
    return final_output

def des_encrypt_block(block, keys):
    permuted_block = initial_permutation(block)
    left_block = permuted_block[:32]
    right_block = permuted_block[32:]
    
    for key in keys:
        next_left_block = right_block
        next_right_block = [l ^ f for l, f in zip(left_block, f_function(right_block, key))]
        left_block = next_left_block
        right_block = next_right_block
    
    final_block = final_permutation(right_block + left_block)
    return final_block

def string_to_bits(string):
    bits = [bin(ord(char))[2:].zfill(8) for char in string]
    return [int(bit) for char_bits in bits for bit in char_bits]

def bits_to_string(bits):
    chars = [chr(int(''.join(map(str, bits[i:i+8])), 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def pad_bits(bits):
    while len(bits) % 64 != 0:
        bits.append(0)
    return bits

def des_encrypt(text, key):
    keys = generate_keys(string_to_bits(key)[:64])
    text_bits = pad_bits(string_to_bits(text))
    encrypted_bits = []
    
    for i in range(0, len(text_bits), 64):
        block = text_bits[i:i+64]
        encrypted_bits.extend(des_encrypt_block(block, keys))
    
    return bits_to_string(encrypted_bits)

def des_decrypt(encrypted_text, key):
    keys = generate_keys(string_to_bits(key)[:64])
    encrypted_bits = string_to_bits(encrypted_text)
    decrypted_bits = []
    
    for i in range(0, len(encrypted_bits), 64):
        block = encrypted_bits[i:i+64]
        decrypted_bits.extend(des_encrypt_block(block, keys[::-1]))
    
    return bits_to_string(decrypted_bits).rstrip('\x00')

# مثال استفاده:
#plain_text = "Hello, World!"
plain_text = input("say somthing: ")
key = "mysecret"

print("پیام اصلی:", plain_text)

encrypted_text = des_encrypt(plain_text, key)
print("پیام رمزنگاری شده:", encrypted_text)

decrypted_text = des_decrypt(encrypted_text, key)
print("پیام بازگشایی شده:", decrypted_text)
