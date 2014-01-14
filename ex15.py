# from sys import argv
# 
# script, filename = argv
# 
# txt = open(filename)
# 
# print "here your file %r:" % filename
# print txt.read()
# 
# print "type the filename again:"
# file_again = raw_input("> ")
# 
# txt_again = open(file_again)
# print txt_again.read()

from sys import argv

script, filename = argv

text = open(filename)

print "here your file %r:" % filename
print text.read()

print "type the filename again:"
file_again = raw_input("> ")

text_again = open(file_again)
print text_again.read()