# from sys import argv
# 
# script, input_file = argv
# 
# def print_all(f):
#     print f.read()
#     
# def rewind(f):
#     f.seek(0)
#     
# def print_a_line(line_count, f):
#     print line_count, f.readline()
# 
# current_file = open(input_file)
# 
# print "first lets print the whole file:\n"
# 
# print_all(current_file)
# 
# print "now lets rewind, kind of like a tape or reverse it back"
# 
# rewind(current_file)
# 
# print "lets print three lines:"
# 
# current_line = 1
# print_a_line(current_line, current_file)
# 
# current_line = current_line + 1
# print_a_line(current_line, current_file)
# 
# current_line = current_line + 1
# print_a_line(current_line, current_file)

from sys import argv

script, input_file = argv

# make a function and giving a command f to a file
def print_all(f):
    print f.read() # telling to read the file will be given

def rewind(f): #telling to rewint the file given
    f.seek(0) 
    
def print_a_line(line_count, f): #telling to count the line of the given file
    print line_count, f.readline(), #telling to line count the file
    
current_file = open(input_file) #telling to open the file, given while executed the script

print "first let print the whole file:\n" #giving a break

print_all(current_file) #calling the current_file which one we just read, to requesting to print

print "how lets rewind the file like a tape"

rewind(current_file) #requesting to rewint the file, thus we can read with numbers

print "lets print three lines:"

current_line = 1
print_a_line(current_line, current_file) #we have given current line = 1, so current_line (1) to open current)file input given to read

current_line = current_line + 1 # here we are giving current_line to add 1 to get next (2nd line)
print_a_line(current_line, current_file)

current_line = current_line + 1 # here we are giving current line_ to read the 3rd line. 
print_a_line(current_line, current_file)  