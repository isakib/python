print "lets pratice everything"
print "you\d' need to know \'bout escapes with \\ that do \n newlines and \t tabs"

poem = """

\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intution
and requires and explanation
\n\t\twherethere is none.
"""

print "----------"
print poem
print "----------"

five = 10 - 2 + 3 - 6
print "this should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jars / 100
    crates = jars / 100
    retrn = jelly_beans, jars, crates
    
start_point = 10000
beans, jars, crates, = secret_formula(start_point)

print "with a starting point of: %d" start_point
print "we have %d beans, %d jars, and %d crates" % secret_formula(start_point)