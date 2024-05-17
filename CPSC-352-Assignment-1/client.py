from socket import *
from sys import *
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Cryptodome.Cipher import AES
SERVER_IP = argv[1] #arg 1 is IP adress
PORT_NUMBER = int(argv[2]) #arg 2 is port numbers
ENCRYPTION_KEY = argv[3].encode() #arg 3 is encryption key



cliSock = socket(AF_INET, SOCK_STREAM)
cliSock.connect((SERVER_IP, PORT_NUMBER))

msg = input("Please enter a message to send to the server: ")
paddedMsg = pad(msg.encode(), 16) 	# Pads the text to be a multiple of 16 bytes
encCipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
cipherText = encCipher.encrypt(paddedMsg)
cliSock.send(cipherText)



cliSock.close()












