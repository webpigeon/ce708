#! /usr/bin/env python3

import string
import python_crypt
import sys

def rotate(l, shift):
	return dict(zip(l, l[shift:]+l[:shift]))

def calc_freq(text):
	"""you may need to modify this if you only care about letters..."""
	f = {}
	for c in text:
		if c in f:
			f[c] += 1
		else:
			f[c] = 1
	return f

def do_subst():
	"""Substution cypher test - very basic as it only support shifts"""
	plain_text = input("enter your plain text ")
	shift_val = int(input("enter your shift value "))
	key = rotate(string.ascii_lowercase, shift_val)
	
	cipher_text = python_crypt.encrypt_subst(plain_text, key)
	decoded_text = python_crypt.decrypt_subst(cipher_text, key)

	print("encrypted text: "+cipher_text)
	print("decrypted text: "+decoded_text)

def do_subst_file():
	"""Substution cypher test - very basic as it only support shifts"""
	filename = input("enter a filename (plain text): ")
	with open(filename) as f:
		plain_text = "".join(f.readlines())

	shift_val = int(input("enter your shift value "))
	key = rotate(string.ascii_lowercase, shift_val)

	filename = input("enter a filename to save to: ")
	cipher_text = python_crypt.encrypt_subst(plain_text, key)
	with open(filename, "w") as f:
		f.write(cipher_text)

def subst_key():
	"""generate a substitution cypher key"""
	key = python_crypt.generate_key()
	print("the generated key is: {}".format(key))

def subst_attack():
	"""attack a substition cypher using freq. analysis"""
	cipher_text = input("enter the cipher text: ")
	hist = calc_freq(input("enter some text for frequencies: "))
	key = python_crypt.attack_subst(cipher_text, hist)
	print("the recovered key is: {}".format(key))

def subst_attack_file():
	"""attack a substition cypher using freq. analysis"""
	filename = input("enter a filename (cipher text): ")
	with open(filename) as f:
		cipher_text = "".join(f.readlines())

	# as above, but with a file
	filename = input("enter a filename (plain text): ")
	with open(filename) as f:
		text = "".join(f.readlines())
	hist = calc_freq(text)

	key = python_crypt.attack_subst(cipher_text, hist)
	print("the recovered key is: {}".format(key))

def do_otp():
	"""Substution cypher test - very basic as it only support shifts"""
	plain_text = input("enter your plain text ")
	key = python_crypt.generate_otp(len(plain_text))
	
	cipher_text = python_crypt.encrypt_otp(plain_text, key)
	decoded_text = python_crypt.decrypt_otp(cipher_text, key)

	print("encrypted text: {}".format(cipher_text))
	print("decrypted text: {}".format(decoded_text))

if __name__ == '__main__':
	choices = {
		"ex1": do_subst,
		"ex2": subst_key,
		"ex3": subst_attack,
		"ex4": subst_attack_file,
		"otp": do_otp,
		"file": do_subst_file
	}
	while True:
		menu_choice = input("enter a choice: ")
		if menu_choice in ["exit", "quit", "q", "ex"]:
			sys.exit(0)

		if menu_choice not in choices:
			print("sorry, that's not a valid choice, choices are: %s" % (", ".join(sorted(choices.keys())),))
		else:
			choices[menu_choice]()
