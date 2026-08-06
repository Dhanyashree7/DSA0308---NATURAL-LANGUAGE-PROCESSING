def plural(noun):

    if noun.endswith("y"):
        return noun[:-1] + "ies"

    elif noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"

    else:
        return noun + "s"
nouns = ["cat", "dog", "box", "bus", "baby", "watch"]

print("Singular\tPlural")

for word in nouns:
    print(word, "\t\t", plural(word))
