#! /usr/bin/env python3

# Exercise 1
#
# Implement a substitution cipher using Python dictionaries.
# You should write two functions: an encrypt_subst function which takes some plain-text, and a key, and returns the cipher-text.
# Similarly write a decrypt_subst function which takes some cipher-text, and a key, and returns the plain-text.

def encrypt_subst(text, key):
	cipher_text = ""
	return cipher_text

def decrypt_subst(cipher, key):
	plain_text = ""
	return plain_text

#
# This should also work... 
#   but for the lab it's better if you write it "the long way" yourself :)
#
# def decrypt_lazy(cipher, key):
#	inv_key = dict( [(v,k) for k, v in key.items()] )
#	return encrypt_subst(cipher, inv_key)
#

# Exercise 2
#
# Write a function to generate a (non-securely generated) random key for your substitution cipher.
# You may make use of the shuffle() function in the module numpy.random.

def generate_key():
	return {}

# Exercise 3
#
# Write a function called attack_subst to recover the key given some cipher-text using a frequency analysis attack.
def attack_subst(cipher, hist):
	return {}

# Exercise 5
#
# Write a Python function to implement a secure one-time pad.
# write an encrypt_otp and a decrypt_otp function which take (plain/cipher) text and a key as an arguments.

def encrypt_otp(text, key):
	cipher_text = ""
	return cipher_text

def decrypt_otp(text, key):
	plain_text = ""
	return plain_text

# Exercise 6
#
# Write a Python function to generate a random OTP key of arbitrary-length by making use of `/dev/urandom'.
# Use this function to encrypt "On the Origin of Species".

def generate_otp(length):
	return []
