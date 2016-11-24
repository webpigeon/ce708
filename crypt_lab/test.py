#! /usr/bin/env python3
##
# Unit tests for Ex1
#
# I'm not providing automated tests for any of the others as they are
# much harder to test correctly. Instead, I've provided an interactive
# runner :).
##

import unittest
import python_crypt
import string

def identity(l):
	return dict(zip(l,l))

def rotate(l, shift):
	return dict(zip(l, l[shift:]+l[:shift]))

class TestEx1(unittest.TestCase):

	def test_ex1_encrypt_identity(self):
		plain_text = "hello world"
		cypher_text = "hello world"
		key = identity(string.ascii_lowercase)
		result = python_crypt.encrypt_subst(plain_text, key)

		self.assertEqual(result, cypher_text)

	def test_ex1_encrypt_rot13(self):
		plain_text = "hello world"
		cypher_text = "uryyb jbeyq"
		key = rotate(string.ascii_lowercase, 13)
		result = python_crypt.encrypt_subst(plain_text, key)

		self.assertEqual(result, cypher_text)

	def test_ex1_encrypt_special(self):
		plain_text = "hello, world!"
		cypher_text = "uryyb, jbeyq!"
		key = rotate(string.ascii_lowercase, 13)
		result = python_crypt.encrypt_subst(plain_text, key)

		self.assertEqual(result, cypher_text)

	def test_ex1_decrypt_identity(self):
		plain_text = "hello world"
		cypher_text = "hello world"
		key = identity(string.ascii_lowercase)
		result = python_crypt.encrypt_subst(cypher_text, key)

		self.assertEqual(cypher_text, plain_text)

	def test_ex1_decrypt_rot13(self):
		plain_text = "hello world"
		cypher_text = "uryyb jbeyq"
		key = rotate(string.ascii_lowercase, 13)
		result = python_crypt.decrypt_subst(cypher_text, key)

		self.assertEqual(plain_text, plain_text)

	def test_ex1_decrypt_special(self):
		plain_text = "hello, world!"
		cypher_text = "uryyb, jbeyq!"
		key = rotate(string.ascii_lowercase, 13)
		result = python_crypt.decrypt_subst(cypher_text, key)

		self.assertEqual(result, plain_text)

	def test_ex1_encrypt_special_nonsym(self):
		plain_text = "if this works, you're probably doing ok :)"
		cypher_text = "yv jxyi mehai, oek'hu fherqrbo teydw ea :)"
		key = rotate(string.ascii_lowercase, 16)
		result = python_crypt.encrypt_subst(plain_text, key)

		self.assertEqual(result, cypher_text)

	def test_ex1_decrypt_special_nonsym(self):
		plain_text = "if this works, you're probably doing ok :)"
		cypher_text = "yv jxyi mehai, oek'hu fherqrbo teydw ea :)"
		key = rotate(string.ascii_lowercase, 16)
		result = python_crypt.decrypt_subst(cypher_text, key)

		self.assertEqual(result, plain_text)

if __name__ == '__main__':
	unittest.main()
