"""
Vigenere Function

string = string to be (en/de)ciphered
key    = key for (en/de)ciphering the string
mode   = accepted values are 1 (encipher) and -1 (decipher)
       = multiplied with the key

http://ja.wikipedia.org/wiki/Vigenere_cipher
"""
def vigenere(string, key, mode = 1):
    return ''.join([[string[i], chr((((ord(string[i].upper())-65)+(ord(key[i%len(key)].upper())-65)*mode)%26)+65)][string[i].isalpha() and key[i%len(key)].isalpha()] for i in range(len(string))])
