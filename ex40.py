class Talk(object):

    def __init__(self, speech):
        self.speech = speech

    def talk_to_me(self):
        for line in self.speech:
            print line

talk_one = Talk(["Express gratitude before speech",
                 "Make dua before starts"])

talk_two = Talk(["Put efforts to understand is saying",
                 "Communcation matters for the leaders"])

talk_one.talk_to_me()
talk_two.talk_to_me()

class Voice(object):

    def __init__(self, voice):
        self.voice = voice

    def voice_over_me(self):
        for line in self.voice:
            print line

voice_one = Voice(["Echo Voice and repeated voice",
                 "ends with it and repeats to starts"])

voice_one.voice_over_me()