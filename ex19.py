# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print "you have %d cheeses" % cheese_count
#     print "you have %d boxes of crackers!" % boxes_of_crackers
#     print "man that's enough for party"
#     print "get a blanket.\n"
# 
# print "we can just give the function numbers directly:"
# cheese_and_crackers(20, 30)
# 
# print "OR, we can use variables from script:"
# amount_of_cheese = 10
# amount_of_crackers = 50
# 
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# 
# print "we can even do math inside too:"
# cheese_and_crackers(10 + 20, 5 + 6)
# 
# print "and we can combine the two, variables and math"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
def number_of_questions_and_marks(number_of_questions, marks_in_exam):
    print "I have got %d questions" % number_of_questions
    print "I have got %d marks for the questions" % marks_in_exam
    print "get the exam done for good marks"
    print "enjoy the exam period"
    
print "we can just give the function numbers directly"
number_of_questions_and_marks(5,10)

print "OR, we can use variable from the script:"
number_questions = 10
marks_exam = 5
#comments
number_of_questions_and_marks(number_questions, marks_exam)

print "we can do some total questions and marks calcuation too"
number_of_questions_and_marks (5 + 10, 10 + 5)

print "and we can combine the two variables and do some math"
number_of_questions_and_marks(number_questions + 100, marks_exam + 50)