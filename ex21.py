def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d + %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d + %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
print "lets do some math with just functios"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "age: %d, height: %d, weight: %d, id: %d" % (age, height, weight, iq)

#a puzzle for extra credit, type it in anyway

print "here is the puzzle"

a_number = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "that becomes: ", a_number, "can you do it by hand?"

#enjoying it, although in rush
