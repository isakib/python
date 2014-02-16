j = 0
numbers = []

while j < 6:
    print "at the top K is %d" % j
    numbers.append(j)
    
    j = j + 200
    print "numbers now: ", numbers #calling the number = [] through that number
    print "at the bottom L is %d" % j
    
print "the numbers:"

for num in numbers:
    print num