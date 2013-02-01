"""
ROT13 Function

string = string to be (en/de)ciphered
mode   = accepted values are 1 (encipher) and -1 (decipher)
       = multiplied with the key

http://ja.wikipedia.org/wiki/ROT13
"""
def rot13(string, mode = 1):
    return ''.join([[s, chr((((ord(s)-[97, 65][s.isupper()])+13*mode)%26)+[97, 65][s.isupper()])][s.isalpha()] for s in string])
