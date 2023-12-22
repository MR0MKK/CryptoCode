LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_cipher(message, key, MODE):
	translated = []
	keyIndex = 0
	key = key.upper()

	for symbol in message:
		num = LETTERS.find(symbol.upper())
		if num != -1:
			if MODE.upper() == 'ENCRYPT':
				num += LETTERS.find(key[keyIndex])
			elif MODE.upper() == 'DECRYPT':
				num -= LETTERS.find(key[keyIndex])
			num %= len(LETTERS)

			if symbol.isupper():
				translated.append(LETTERS[num])
			elif symbol.islower():
				translated.append(LETTERS[num].lower())

			keyIndex += 1
			if keyIndex == len(key):
				keyIndex = 0
		else:
			translated.append(symbol)
	return ''.join(translated)


def main():
	message = "My name is Minh and I'm student."

	key = 'minhkingkong'
	cipher = vigenere_cipher(message, key, 'ENCRYPT')
	print('Message:               ' + message + "\n")
	print('Ciphertext:            ' + cipher+ "\n")

	message = vigenere_cipher(cipher, key, 'DECRYPT')
	print('Message after decrypt: ' + message+ "\n")


if __name__ == '__main__':
	main()