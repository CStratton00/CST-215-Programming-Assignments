file = open("/Users/collinstratton/Google Drive/School/GCU/Freshmen/CST-215/encryptmessage.txt", "r")
text = file.readline()
text = text.strip()

key = int(input("Caesar Cypher Key: "))

encryptedMessage = ""
for ch in text:
    code_val  = ord(ch) + key
    if ch.isalpha():
        if code_val > ord('z'):
            code_val -= ord('z') - ord('a')
        encryptedMessage = encryptedMessage + chr(code_val)
    else:
        encryptedMessage = encryptedMessage + ch

print(text)
print(encryptedMessage)
