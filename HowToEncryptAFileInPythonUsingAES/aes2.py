### To install the pycryptodome library ####
# sudo apt install python3-pip
# sudo pip3 install pycryptodomex

from Cryptodome.Cipher import AES

######### BASIC ENCRYPTION ###########

# The key (must be 16 bytes)
key = b'Sixteen byte key'

# Set up the AES encryption class
encCipher = AES.new(key, AES.MODE_ECB)

# AES requires plain/cipher text blocks to be 16 bytes
cipherText = encCipher.encrypt(b'Hello world there is a world full of programmers')

print("Cipher text: ", cipherText)

file = open("myEncFile.bin", "wb").write(cipherText)

########### BASIC DECRYPTION ##############

# Set up the AES encryption class
#decCipher = AES.new(key, AES.MODE_ECB)

#cipherText = open("encfile.bin", "rb").read()

# AES requires plain/cipher text blocks to be 16 bytes
#plainText = decCipher.decrypt(cipherText)


#open("decfile.bin", "wb").write(plainText)
#print("Decrypted text: ", plainText)
