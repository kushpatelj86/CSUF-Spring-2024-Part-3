all:	des

des:	des.o
	gcc des.o -o des -lcrypto -lssl

des.o:	des.c
	gcc -c des.c

clean:
	rm -rf *.o des


