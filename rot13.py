"""
ROT13 Function

string = string to be (en/de)ciphered

http://ja.wikipedia.org/wiki/ROT13
"""
def rot13(string):
    return ''.join([[s, chr((((ord(s)-[97, 65][s.isupper()])+13)%26)+[97, 65][s.isupper()])][s.isalpha()] for s in string])
