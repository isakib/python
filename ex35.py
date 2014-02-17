from sys import exit

def gold_room(): # once I will get out from the room of bear, I will get into the Gold room.
    print "tons of gold inside the room?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
        
    else:
        dead("man, learn to type a number") # if no numeric data has input given, it will give this messages
        
    if how_much < 50: # if numeric data given, it compares with 50 and give status you're good or bad guy as I have mentioned to "print"
        print "Nice, you're good guy" 
        exit(0)
    
    else:
        dead("Bad, control over your desire - even when you got enough")

def bear_room():
    print "there is a bear here"
    print "How are you going to deal and get out?"
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey": #if I call it, the bear will just slap
            dead("the bear looks at you then slaps off")
        elif next == "shoot bear" and not bear_moved: #as it is and not the when I Have shoot bear, it will show me way out.
            print "the bear has moved from the door, you can go"
            
            bear_moved = True
        elif next == "shoot bear" and bear_moved: # if the def bear_room line 23 I made True, then it will be come and print out the 35 line.
            dead("the bear gets pissed off and chews the leg")
        elif next == "open door" and bear_moved: #once I have open the door, I will be enter into gold room function called def gold_room()
            gold_room()
        else:
            print "I got no idea what to do"
            
def right_room():
    print "there you can see the great evil"
    print "he, it whatever states at your and you became insane"
    print "do you flee for your life or eat your head"
    right_room = False
    
    next == raw_input("> ")
    
    if next == "flee" and not bear_moved:
        dead("well that was tasty")
    elif next == "head" and bear_moved:
        dead("well that was tasty")
    else:
        right_room("No way out, in stuck RIGHT ROOM")
        
def dead(why):
    print why, "good job"
    exit(0)

def start():
    print "Stuck into a room"
    print "Two options: Left or Right"
    print "Choose 1 side wisely"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        right_room()
    else:
        dead("You're Finished, Man") #if I don't give or call properly, I will be ended here.
        
start()