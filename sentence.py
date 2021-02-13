import random
import words.words as words
import words.add_s as add_s
import words.tools as tools

class sentence:
    def __init__(self):
        self.__words=words.words
    def run(self):
        pattern=random.randint(1,7)
        pattern=7
        if pattern==1:
            #現在形(S+V)
            self.__subject=random.choice(self.__words["subject"])
            self.__verb=random.choice(self.__words["normal_verb"]["normal"])
            if self.__subject in self.__words["be_verb+subject"]["is"]: self.__verb = add_s.add_s(self.__verb)
            return "{} {}.".format(tools.first_upper(self.__subject),self.__verb)
        elif pattern==2:
            #現在形(Do S+V)
            self.__subject=random.choice(self.__words["subject"])
            self.__verb=random.choice(self.__words["normal_verb"]["normal"])
            if self.__subject in self.__words["be_verb+subject"]["is"]: self.__verb = add_s.add_s(self.__verb)
            if self.__subject == "i": self.__subject=tools.first_upper(self.__subject)
            return "Do {} {}?".format(self.__subject,self.__verb)
        elif pattern==3:
            #現在形(S do(es)n't V)
            self.__subject=random.choice(self.__words["subject"])
            self.__verb=random.choice(self.__words["normal_verb"]["normal"])
            if self.__subject in self.__words["be_verb+subject"]["is"]: return "{} doesn't {}.".format(tools.first_upper(self.__subject),self.__verb)
            return "{} don't {}.".format(tools.first_upper(self.__subject),self.__verb)
        elif pattern==4:
            #現在形(S+V+O)
            self.__subject=random.choice(self.__words["subject"])
            self.__verb=random.choice(self.__words["normal_verb"]["special"])
            self.__noun=random.choice(self.__words["noun"][self.__verb[1]])
            self.__verb=self.__verb[0]
            if self.__subject in self.__words["be_verb+subject"]["is"]: self.__verb = add_s.add_s(self.__verb)
            return "{} {} {}.".format(tools.first_upper(self.__subject),self.__verb,self.__noun)
        elif pattern==5:
            #現在形(Do S+V+O)
            self.__subject=random.choice(self.__words["subject"])
            self.__verb=random.choice(self.__words["normal_verb"]["special"])
            self.__noun=random.choice(self.__words["noun"][self.__verb[1]])
            self.__verb=self.__verb[0]
            if self.__subject in self.__words["be_verb+subject"]["is"]: self.__verb = add_s.add_s(self.__verb)
            if self.__subject == "i": self.__subject=tools.first_upper(self.__subject)
            return "Do {} {} {}?".format(self.__subject,self.__verb,self.__noun)
        elif pattern==6:
            #現在形(S do(es)n't V+O)
            self.__subject=random.choice(self.__words["subject"])
            self.__verb=random.choice(self.__words["normal_verb"]["special"])
            self.__noun=random.choice(self.__words["noun"][self.__verb[1]])
            self.__verb=self.__verb[0]
            if self.__subject in self.__words["be_verb+subject"]["is"]: return "{} doesn't {} {}.".format(tools.first_upper(self.__subject),self.__verb,self.__noun)
            return "{} don't {} {}.".format(tools.first_upper(self.__subject),self.__verb,self.__noun)
        elif pattern==7:
            #現在形(S+V+O)be動詞
            self.__verb=random.choice(self.__words["be_verb"]["normal"])
            self.__subject=random.choice(self.__words["be_verb+subject"][self.__verb])
            self.__noun=random.choice(self.__words["noun"][random.choice(self.__words["be_verb_use_noun"])])
            return "{} {} {}.".format(tools.first_upper(self.__subject),self.__verb,self.__noun)
            


test = 1

if __name__=="__main__" and test==1:
    while True:
        print(sentence().run())
        if input() != "": break