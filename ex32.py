the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'organges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print "this is count %d" % number

#same as above
for fruit in fruits:
    print "a fruit of type: %s" % fruit
    
#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it

for i in change:
    print "I got %r" %i
    
#we can also build lists, first starts with an empty one
elements = []

#then use the range fucntion to do 0 to 5 counts
for i in range(0, 10):
    print "adding %d to the list " % i
    #append is a fucntion that lists understanding
    elements.append(i)
    
#Now we can print them out too
for i in elements:
    print "element was: %d" % i
    
print "-----------------"
print "-----------------"


news = [1, 2, 3, 4, 5]
people_n = ['hik', 'bik', 'kik', 'tik', 'jik']
money = [1, 'dollar', 2, 'pounds', 3, 'taka']

for number in news:
    print "news channel %d " % number
    
for people in people_n:
    print "these are good people %s" % people_n
    
for i in money:
    print "I got enough %r" % money
    
elemtns = []

for i in range(0, 5):
    print "adding %d will continue to add list or expand" % i
    elements.append(i)
    
for i in elements:
    print "elements are: %d" % i