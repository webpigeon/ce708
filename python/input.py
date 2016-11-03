#! /usr/bin/env python3
##
# Python Input Example
##

# use input to get values from the user
name = input("What is your name? ")

# we'll print it out now :)
print("hello, ", name)

# String Formatting

## You can also use formatted strings
print("hello %s" % (name,) ) # method 1: % syntax (older)
print("hello {0}, How are you today?".format(name) ) # using string formatting

# Documentation for .format can be found online: https://docs.python.org/3/library/string.html#format-string-syntax
