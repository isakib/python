cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
# = means, given name have to equal to right side, so that will be interpret while print has executed.
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "there are", cars, "cars available"
print "there are only", drivers, "drivers available"
print "there will be", cars_not_driven, "empty cars today"

# yes because of using 0, result came out with decimal points after actual digits.
print "we can transport", carpool_capacity, "people today"
print "we have", passengers, "to carpool today"
print "we need to put about", average_passengers_per_car, "in each cars" 

#test case
#Traceback (most recent call last):
#      File "ex4.py", line 8, in <module>
 #       average_passengers_per_car = car_pool_capacity / passenger
  #  NameError: name 'car_pool_capacity' is not defined
  
  
  #Solution:
  
  # the only possible reason is, didn't defined anything for that "car_pool_capacity", so while
  # execution done - it got error. 