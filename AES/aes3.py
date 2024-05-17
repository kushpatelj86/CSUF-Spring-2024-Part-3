from Cryptodome.Cipher import AES

key = b'Sixteen byte key'

decCipher = AES.new(key, AES.MODE_ECB)

cipherText = open("myEncFile.bin", "rb").read()

# AES requires plain/cipher text blocks to be 16 bytes
plainText = decCipher.decrypt(cipherText)


open("myDecFile.bin", "wb").write(plainText)
print("Decrypted text: ", plainText)
