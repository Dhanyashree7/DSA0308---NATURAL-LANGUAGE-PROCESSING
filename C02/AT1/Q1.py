words = ["connected", "connecting", "connection"]
print("Word\t\tRoot\tSuffix\tType")
for word in words:
    if word.endswith("ed"):
        print(word,"\tconnect\ted\tInflectional")
    elif word.endswith("ing"):
        print(word,"\tconnect\ting\tInflectional")
    elif word.endswith("ion"):
        print(word,"\tconnect\tion\tDerivational")
