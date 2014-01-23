# from sys import argv
# 
# script, user_name = argv
# prompt = '>'
# 
# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I would like to ask you a few questions"
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)
# 
# print "where do you live %s?" % user_name
# lives = raw_input(prompt)
# 
# print "what kind of computer do you have?"
# computer = raw_input(prompt)
# 
# print """
# 
# Alright, so you said %r about liking me.
# You live in %r. Not sure where is that.
# And you have a %r computer, which is truly powerful machine
# """ % (likes, lives, computer)

from sys import argv

script, username = argv
prompt = '>' 

# it can be anything or any new input you can give, no harms, just it will show where you have to type.

print "Hello Brother %s, I'm script or you can tell me %s" % (username, script)

print "I want to update some stuffs about yourself,"
print "Do you know the meaning of my name?"
meaning = raw_input(prompt)

print "Do you know, where I live or trac me back"
location = raw_input(prompt)

print "Do you know what meaning I do use"
machine_lang = raw_input(prompt)

print "If you get update, make dua for what you've just learned"
make_dua = raw_input(prompt)

print """
Now I know lots of information about you. For example, your name is %r, your location is tracked which is in bansree, capitcal of %r, your machine is %r, and make dua %r
    """ % (username, meaning, machine_lang, make_dua)




