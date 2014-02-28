# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'TX': 'Texas'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 50
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 50
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']
print "California's abbreviation is", states['California']

# do it by using the state then cities dict
print '-' * 50
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
print "California has: ", cities[states['California']]
# print every state abbreviation

print '-' * 50
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)


# print every city in state
print '-' * 50
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 50
for sa, kib in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        sa, kib, cities[kib])

print '-' * 50
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

