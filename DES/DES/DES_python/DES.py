from Crypto.Cipher import DES

# Create an instance of the DES class
# and initialize the key
des = DES.new('13371337', DES.MODE_ECB)

# The plaintext
plainText = "BillyBob"

print("Plain text: " + plainText)

# Encrypt the plaintext
cipherText = des.encrypt(plainText)

print ("Cipher text: ", cipherText)

# Decrypt the text
print ("Decrypted text: ", des.decrypt(cipherText))






