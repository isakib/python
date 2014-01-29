print "lets do a pratice"
print "I'm trying to learn a language with some good intentions, O Allah you help me"

story = """
A boy who lives in Dhaka, 
Spending simple life, Alhamdulliah
Looking for better life here and hereafter
Concern about things which people ignore
"""

print "---------------"
print story
print "---------------"

six = 10 - 2 + 3 - 6
print "this should be six in amount %s:" % six

def my_formula(started):
    people = started * 500
    books = people / 1000
    ink = books / 100
    return people, books, ink
    
starting_amount = 1000
people, books, ink = my_formula(starting_amount)

print "with a starting point of: %d" % starting_amount
print "we would like to %d people, to write %d books, with %d  amount of ink" % (people, books, ink)

starting_amount = starting_amount / 10

print "we can also do this way:"
print "we have %d of pens, %d of books, and %d of ink pots" % my_formula(starting_amount)
































# print "lets pratice everything"
# print "you'd need to know about escapes with \\ that do \n newlines and \t tabs"
# 
# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intution
# and requires and explanation
# \n\t\twherethere is none.
# """
# 
# print "----------"
# print poem
# print "----------"
# 
# five = 10 - 2 + 3 - 6
# print "this should be five: %s" % five
# 
# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates
#     
# start_point = 10000
# beans, jars, crates, = secret_formula(start_point)
# 
# print "with a starting point of: %d" % start_point
# print "we'd have %d beans, %d jars, and % creates" % (beans, jars, crates)
# 
# start_point = start_point / 10
# 
# print "we can also do that this way:"
# print "we'd have %d beans, %d jars, and %d crates" % secret_formula(start_point)