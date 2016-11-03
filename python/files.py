#! /usr/bin/env python3
##
# Python File Example
##

# note: there are better (and easier) ways to write this
# I'm writing it this way to demonstate some features :)
def get_lines(filename):
	"""Read in a file line by line and return it as an array"""
	lines = [] # create variables by giving them a value (varibles have no types)

	# with means that files are closed correctly if our program throws an error (you should use it!)
	with open(filename, "rt") as file:
		# You can loop though files line by line using a for loop
		for line in file:
			lines.append(line)

	return lines

# incase anyone is intrested, here is a better version
def get_lines2(filename):
	"""read lines from a file"""
	with open(filename, "rt") as file:
		return file.readlines()

print(get_lines("test"))
print(get_lines2("test"))
