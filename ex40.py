class Talk(object):

    def __init__(self, speech):
        self.speech = speech

    def teach_me_speech(self):
        for line in self.speech:
            print line

print "DAY ONE:"
print "--" * 10


day_one = Talk(["Say As Salam",
                "Say How Are You Brother",
                "Say Sounds Good"])

day_two = Talk(["Second Day:"
                "Say Waalikumus Salam",
                "Alhamdulliah, I'm fine"])

day_one.teach_me_speech()


day_two.teach_me_speech()
