print "2 room booking options you have, choose good one?"

room = raw_input("> ")

if room == "1":
    print "there is a big large room for couple, what inside the room?"
    print "1. A large bed room"
    print "2. A large garden infront of the room"
    
    room = raw_input("> ")
    
    if room == "1":
        print "that room is best"
    elif room == "2":
        print "that is good for both of us"
    elif room == "3":
        print "BEST OF BEST"
    elif room == "0":
        print "Heh, Got Zero"
    else:
        print "well, I guess %s in both side is best suit for us" % room
        
elif room == "2":
    print "there is a small room for couble, what's inside the room, lets explose:"
    print "1. Small room but good environment"
    print "2. Small room but large kitchen"
    
    features = raw_input("> ")
    
    if features == "1" or features == "2":
        print "you have good a nice room, great job"
    else:
        print "you have got avg good room, %s" % features
             
else:
    print "nice home atleast at first we are in trip, right :)"

# print "you enter a dark room with two doors. Do you go through door #1 or door #2?"
# 
# door = raw_input("> ")
# 
# if door == "1":
#     print "there is a giant bear here eating a cheese cake, what do you do?"
#     print "1. take the cake"
#     print "2. scream at the bear"
#     
#     bear = raw_input("> ")
#     
#     if bear == "1":
#         print "the bear eats your face off, good job"
#     elif bear == "2":
#         print "the bear eats your legs off, good job"
#     else:
#         print "well, doing %s is probably better, bear runs away" %bear
#         
#     
# elif door == "2":
#     print "you stare into the endless abyss at Cthulhu's retina"
#     print "1. Blueberries"
#     print "2. Yellow Jacket clothespins"
#     print "3. Understanding revolvers yelling melodies"
#     
#     insanity = raw_input("> ")
#     
#     if insanity == "1" or insanity == "2":
#         print "your body survives powered by a mind of jello, good job"
#     else:
#         print "the insaity rots your eyes into a pool of muck, good job"
#         
# else:
#     print "you stumble around and fall on a knife and die, good job"