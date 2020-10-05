import os
import random

def cipher(l):
	cip = ""
	lg = len(key)
	t = ""
	for i in range(len(l)):
		t+= chr(ord(l[i])^ord(key[i%lg]))

	return t

key = ""
while len(key) < 1:
	key = input('Enter Password: ')

path = input('Enter Folder Path: ')

F = []
files = os.listdir(path)
cur_path = os.path.dirname(__file__)
path = os.path.join(cur_path , path)
for file in files:
	p = os.path.join(path , file)
	if file.endswith('.txt'):
		with open(p,'r') as f:
			l = f.read()
			l = cipher(l)
			print(str(l))
			F.append(l)
			# l = cipher(l)
			
for file in files:
	p = os.path.join(path , file)
	if file.endswith('.txt'):
		with open(p,'w') as f:
			f.truncate(0)
			f.write(F[0])
			F.pop(0))

'''

Cool Fact : You can decrypt the encrypted message with the same code, just give the message to decrypt as the input and give the same key which was use for
encryption.

'''
