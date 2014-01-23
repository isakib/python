# # this one is like your scripts with argv
# def print_two(*args):
#     arg1, arg2, arg3, arg4 = args
#     print  "arg1: %r, arg2: %r, arg3: %r, arg4: %r" % (arg1, arg2, arg3, arg4)
# 
# #ok, that *args is actually pointless, we can just do this
# def print_two_again(arg1, arg2, arg3): 
#     print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)
#     
# #this is just takes one argument
# def print_one(arg2):
#     print "arg2: %r" % arg2 
#     
# #this one takes no arguments
# def print_none():
#     print "I got nothing'."
#     
# print_two("ONE", "TWO", "THREE")
# print_two_again("One", "Two", "Three")
# print_one("NEW")
# print_none()

def print_my_full_name(*args):
    arg1, arg2, arg3, arg4 = args
    print  "arg1: %r, arg2: %r, arg3: %r, arg4: %r" % (arg1, arg2, arg3, arg4)
    
def print_multiple_argument(arg1, arg2, arg3):
    print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)
    
def print_single(arg2):
    print "arg2: %r" % (arg2)
    
def print_none():
    print "I got nothing"

print_my_full_name("Sakib", "Al", "Mahmud", "Full Name")
print_multiple_argument("SAKIB", "AL", "MAHMUD")
print_single("SINGLE")
print_none()