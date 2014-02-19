from sys import exit

def gold_room():
    print "this room is full of gold, how much do you take?"
    
    next == raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        msg("man, learn to type number")
        
    if how_much < 50:
        print "Good guy, who got control over desire"
        exit(0)
    else:
        msg("Bad guy, who got no control over desire")
        
def left_room():
    print "you will find a bear"
    print "how you will skip that bear, without facing bear"
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        if next == "food":
            msg("bear will eat you as food")
        elif next == "shoot bear" and not bear_moved:
            msg("the bear died, now you can go through")
        elif next == "shoot bear" and bear_moved:
            msg("the bear is out of control and get into for attack")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "What the HECK?"
            
def right_room():
    print "Now you're in trouble room"
    print "How you should skip that situation: Flee?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        msg("well that was delicious")
    else:
        right_room()
        
def msg(why):
    print why, "Great, job"
    exit(0)
    
def start():
    print "you are in dark room"
    print "take left/right side?"
    
    next = raw_input("> ")
    
    if next == "left":
        left_room()
    elif next == "right":
        right_room()
    else:
        msg("You're in danger") 
    
start()       


        #fails