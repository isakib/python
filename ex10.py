tabby_cat = "\tI'm tabbed in."
persian_cat = "\tI'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
right_cat = "I do // things"
night_mode = "I do \n now"
base_mode = "trying to shift \bmode"

fat_cat = '''
I'll do a list now - below there are strings:

\t* cat food
\t* fishes
\t* catnip\n\t* Grass
Sub issues:
\t* Sub list\n\t\t 1st one\n\t\t 2nd one
'''

print tabby_cat
print persian_cat
print backslash_cat
print "." * 20
print fat_cat
print "." * 20 
print right_cat
print night_mode
print base_mode

print "." * 20 

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
