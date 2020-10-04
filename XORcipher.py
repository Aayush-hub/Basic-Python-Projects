def XORcipher(text,key):
	
	encrypted_text = ""

	for i in range(len(text)):

		encrypted_text += chr(ord(text[i]) ^ ord(key))

	return  encrypted_text

text = input('Enter message to encrypt or decrypt : ')

key = input('Enter a key : ')


print(XORcipher(text,key))

'''

Cool Fact : You can decrypt the encrypted message with the same code, just give the message to decrypt as the input and give the same key which was use for
encryption.

'''
