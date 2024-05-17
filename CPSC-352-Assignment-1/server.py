from socket import *
from sys import *
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Cryptodome.Cipher import AES



PORT_NUMBER = int(argv[1]) #arg 1 is port numbers
DECRYPTION_KEY = argv[2].encode() #arg 2 is decryption  key

serverSock = socket(AF_INET, SOCK_STREAM) 
serverSock.bind(('', PORT_NUMBER)) 
serverSock.listen(100)


while True:
	print("Waiting for clients to connect...")
	cliSock, cliInfo = serverSock.accept()
	print("Client connected from: " + str(cliInfo))
	cliMsg = cliSock.recv(16)	
	print("Client sent " + str(cliMsg))
	#encCipher = AES.new(key, AES.MODE_ECB)
	#cipherText = encCipher.encrypt('h4jlf123fj676s0d1114311150114s11f2')
	#print("Cipher text: ", key)
	decCipher = AES.new(DECRYPTION_KEY, AES.MODE_ECB)
	plainText = decCipher.decrypt(cliMsg)
	#unpaddedDecryptedText = unpad(plainText,16)
	print("Decrypted text: ", plainText.decode())
	cliSock.close()

