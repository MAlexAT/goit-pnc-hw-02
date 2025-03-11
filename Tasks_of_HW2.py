import numpy as np

# 1. Шифр Віженера
def vigenere_encrypt(text, key):
    key = key.upper()
    text = text.upper()
    encrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(text, key):
    key = key.upper()
    text = text.upper()
    decrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

# 2. Шифр перестановки
def simple_transposition_encrypt(text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = (len(text) + num_columns - 1) // num_columns
    padded_text = text.ljust(num_rows * num_columns, 'X')
    matrix = [list(padded_text[i:i+num_columns]) for i in range(0, len(padded_text), num_columns)]
    encrypted_text = "".join("".join(row[i] for row in matrix) for i in key_order)
    return encrypted_text

def simple_transposition_decrypt(text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = len(text) // num_columns
    matrix = [[''] * num_columns for _ in range(num_rows)]
    index = 0
    for i in key_order:
        for row in range(num_rows):
            matrix[row][i] = text[index]
            index += 1
    decrypted_text = "".join("".join(row) for row in matrix).rstrip('X')
    return decrypted_text

# 3. Табличний шифр
def matrix_cipher_encrypt(text, key):
    key_length = len(key)
    grid_size = (len(text) + key_length - 1) // key_length * key_length
    text = text.ljust(grid_size, 'X')
    matrix = np.array(list(text)).reshape(-1, key_length)
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    encrypted_text = "".join("".join(matrix[:, i]) for i in key_order)
    return encrypted_text

def matrix_cipher_decrypt(text, key):
    key_length = len(key)
    num_rows = len(text) // key_length
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    matrix = np.array(list(text)).reshape(key_length, num_rows).T
    decrypted_matrix = np.empty((num_rows, key_length), dtype=str)
    for i, index in enumerate(key_order):
        decrypted_matrix[:, index] = matrix[:, i]
    decrypted_text = "".join("".join(row) for row in decrypted_matrix)
    return decrypted_text.rstrip('X')

# Виконання завдання
with open("text_input.txt", "r", encoding="utf-8") as file:
    test_text = file.read().strip()
    
key_vigenere = "CRYPTOGRAPHY"
key_transposition = "SECRET"
key_matrix = "MATRIX"

# Використання шифру Віженера
vigenere_encrypted = vigenere_encrypt(test_text, key_vigenere)
vigenere_decrypted = vigenere_decrypt(vigenere_encrypted, key_vigenere)

# Використання шифру перестановки
transposition_encrypted = simple_transposition_encrypt(test_text, key_transposition)
transposition_decrypted = simple_transposition_decrypt(transposition_encrypted, key_transposition)

# Використання табличного шифру
matrix_encrypted = matrix_cipher_encrypt(test_text, key_matrix)
matrix_decrypted = matrix_cipher_decrypt(matrix_encrypted, key_matrix)

# Вивід результатів
print("Шифр Віженера:")
print("Зашифрований текст:", vigenere_encrypted)
print("Розшифрований текст:", vigenere_decrypted)
print()
print("Шифр перестановки:")
print("Зашифрований текст:", transposition_encrypted)
print("Розшифрований текст:", transposition_decrypted)
print()
print("Табличний шифр:")
print("Зашифрований текст:", matrix_encrypted)
print("Розшифрований текст:", matrix_decrypted)
