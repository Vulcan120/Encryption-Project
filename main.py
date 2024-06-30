from string import ascii_lowercase
import random

alpha = list(ascii_lowercase)
plaintext = "antidisestablishmentarianism"
ciphertext = "annettmaihrdsiiiaslnebisastm"

#ONE TIME PAD -----
def OneTimePadEncrypt(plaintext):
	key = "".join([random.choice(alpha) for i in range(len(plaintext))])
	print(plaintext)
	print(key)
	encrypted = "".join([alpha[(alpha.index(letter) + alpha.index(key[l_index]) +1)%26] for l_index, letter in enumerate(plaintext)])		#A (0) + 1 + C(2) = D(3)
	print(encrypted)



def OneTimePadDecrypt(ciphertext):
	key = input("Enter key:").lower()
	
	decrypted = "".join([alpha[(alpha.index(letter) - alpha.index(key[l_index])-1)%26] for l_index, letter in enumerate(ciphertext)])
	print(decrypted)


	
#RAIL FENCE ----------
	
def RailFenceEncrypt(plaintext):
	key = int(input("Enter key:"))
	board = [[" " for i in range(len(plaintext))] for i in range(key)] #creates (key) no of lists with length of plaintext no. of lists inside them
	x = 0
	y = 0
	direction = 1
	for letter in plaintext:
		board[y][x] = letter
		x += 1
		y += direction
		if y >= key-1:
			direction *= -1
		elif y == 0:
			direction *= -1

	for row in board:
		print(row) #prints full board
	print("".join([i for rows in board for i in rows if i != " "]))



def RailFenceDecrypt(ciphertext):
	key = int(input("Key:"))
	decrypted = ""
	
	board = [[" " for i in range(len(plaintext))] for i in range(key)]
	x = 0					#makes a board with Xs as a template
	y = 0
	direction = 1
	for letter in ciphertext:
		board[y][x] = "X"
		x += 1
		y += 1 * direction
		if y == key-1:
			direction *= -1
		elif y == 0:
			direction *= -1
	print(board)
	
	i = 0					#replaces Xs row by row with the cipher text 
	for row_index, row in enumerate(board):
		for col_index, cell in enumerate(row):
			if cell == "X":
				board[row_index][col_index] = ciphertext[i]
				i += 1
	print(board)				

	x = 0
	y = 0
	direction = 1 			#returns plaintext by reading the railfence in zigzag
	for letter in plaintext:
		decrypted += letter
		x += 1
		y += 1 * direction
		if y == key-1:
			direction *= -1
		elif y == 0:
			direction *= -1

	print(decrypted)
			
			
# ENIGMA MACHINE ----------------
def ligmaMachine(message):
	rotors = [
[22,13,19,14,7,11,0,4,24,10,21,6,12,20,15,3,2,1,25,16,17,18,8,5,9,23], #index corresponds to alphabet (e.g. A shifts to 22nd letter in alpha)
[18,14,10,5,4,2,24,8,17,0,25,22,1,6,13,19,12,3,7,20,23,11,21,9,16,15],
[10,22,0,24,5,2,9,14,11,21,6,4,18,1,19,25,12,23,20,17,15,8,3,13,7,16]]

	reflectorA = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	reflectorB = [
'c', 'z', 'a', 'k', 'l', 's', 'u', 'm', 't', 'q', 'd', 'e', 'h', 'v', 'w', 'y', 'j', 'x', 'f', 'i', 'g', 'n', 'o', 'r', 'p', 'b']

	print(message)
	encrypted = message.lower()

	for count1 in range(0,3):
		encrypted = "".join([alpha[rotors[count1][alpha.index(i)]] for i in encrypted])
		print(encrypted)			#changes letter to corresponding letter in rotor
		
	reflected = "".join([reflectorB[reflectorA.index(letter)] for letter in encrypted])
	print(reflected)				#essentially the same as rotor except the letters are in pairs
	
	for count2 in range(2,-1,-1):		
		reflected = "".join([alpha[rotors[count2].index(alpha.index(i))] for i in reflected])
		#finds the number of the letter (A - 1st), finds where in rotor links to that letter, gets the index of it(alphabet corresponds to index)
		print(reflected)



def menu():
	print("1. Rail Fence\n2. One Time Pad\n3. Enigma Machine")
	choice1 = int(input(":"))
	if choice1 in [1,2]:
		choice2 = input("Encrypt or decrypt (E/D)").upper()
	text = input("Enter text:")
	if choice1 == 3:
		ligmaMachine(text)
	elif choice1 == 1 and choice2 == "E":
		RailFenceEncrypt(text)
	elif choice1 == 1 and choice2 == "D":
		RailFenceDecrypt(text)
	elif choice1 == 2 and choice2 == "E":
		OneTimePadEncrypt(text)
	else:
		OneTimePadDecrypt(text)
		
		
menu()
	
