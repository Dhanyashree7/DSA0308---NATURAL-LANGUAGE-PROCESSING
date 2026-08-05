words = ["played", "player", "playing"]
print("Word\t\tStem\tType")
for word in words:
    if word.endswith("ed"):
        stem = word[:-2]
        print(word,"\t",stem,"\tInflectional")
    elif word.endswith("er"):
        stem = word[:-2]
        print(word,"\t",stem,"\tDerivational")
    elif word.endswith("ing"):
        stem = word[:-3]
        print(word,"\t",stem,"\tInflectional")
