LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere(key, message, mode):
    code_text = []
    keyIndex = 0
    key = key.upper()

    for x in message:
        num = LETTERS.find(x.upper())

        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])
            
            num %= len(LETTERS)

            if x.isupper():
                code_text.append(LETTERS[num])
            elif x.islower():
               code_text.append(LETTERS[num].lower())
            
            keyIndex += 1

            if keyIndex == len(key):
                keyIndex = 0

        else:
            code_text.append(x)

    return ''.join(code_text)

message = input("Message to encrypt: ")
key = input("Key: ")
encrypt = "encrypt"
decrypt = "decrypt"

code = str(vigenere(key, message, encrypt))
print(code)
print(vigenere(key, code, decrypt))