#Finding the min and max of the lengths of phrases(character strings)
phrases = ["Hello world", "Breakfast tastes good",
           "Are Pina Coladas salty?", "hi"]
i = 0
phrasesl = len(phrases)
print(phrasesl)
min = len(phrases[0])
max = len(phrases[0])
while i < phrasesl:

    phrase = phrases[i]
    l = len(phrase)
    # test = phrases[i].upper()
    print("phrase", i, phrase, l, "characters")
    if l < min:
        min = l
        print("new min", min)
    else:
        print("no new min")
    if l > max:
        max = l
        print("new max", max)
    else:
        print("no new max")

    i = i+1
print("final min", min,"final max", max)
