special_word={
    "child":"children","man":"men","woman":"women","mouse":"mice","tooth":"teeth","life":"lives","foot":"feat","person":"peaple"
}
not_s_word=[
    "good at","funiture"
]

def add_s(word):
    if word in special_word:
        return special_word[word]
    elif word in not_s_word:
        return word
    elif (word[-1]=="s")or \
        (word[-1]=="z")or \
        (word[-2:]=="sh")or \
        (word[-2:]=="ch")or \
        (word[-1]=="x"):
        return word + "s"
    elif (not(word[-2]=="a" or word[-2]=="i" or word[-2]=="u" or word[-2]=="e" or word[-2]=="o")) and \
        (word[-1]=="o"):
        return word + "es"
    elif (not(word[-2]=="a" or word[-2]=="i" or word[-2]=="u" or word[-2]=="e" or word[-2]=="o")) and \
        (word[-1]=="y"):
        return word[:-1] + "ies"
    elif (word[-1] == "f"):
        return word[:-1] + "ves"
    elif (word[-2:] == "fe") :
        return word[:-2] + "ves"
    else :
        return word + "s"