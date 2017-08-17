# -*- coding: utf-8 -*-
# transposition_cipher.py

def encrypt_message(key, message):
    ciphertext = [''] * key
    ml = len(message)
    for col in range(key):
        pointer = col
        while pointer < ml:
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)

def main():
    m = 'dear baby, i love you.'
    k = 5
    em = encrypt_message(k, m)
    print(em)

if __name__ == '__main__':
    main()
