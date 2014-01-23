from sys import argv

script, filename = argv

print "we are going to erase %r." % filename # I'm setting string here
print "if you don't want that, hit CTRIL-C (^C)."
print "if you do want that, hit RETURN."

raw_input("?") # raw input or anything I can replace with ?

print "Opening the file...." # just a msg to the users
target = open(filename, 'w')

print "truncating the file. Goodbye"
target.truncate()

print "now i'm going to ask you for three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "i'm going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally, we close it"
target.close()