people = 30
cars = 40
buses = 15

if cars > people:
    print "we should take the cars."
elif cars < people:
    print "we should not take the cars."
    
else:
    print "we can't decide it now."

if buses > cars: 
    print "thats too many buses"
    
elif buses < cars:
    print "maybe we could take the buses"
    
else:
    print "we cant still decidide"
    
if people > buses:
    print "alright, lets just take the buses"
    
else:
    print "fine, lets stay home then"