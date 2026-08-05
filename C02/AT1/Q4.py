words = ["writes","writing","written"]
print("Word\t\tRoot\tType")
for word in words:
    if word == "writes":
        print(word,"\twrite\tRegular")
    elif word == "writing":
        print(word,"\twrite\tRegular")
    elif word == "written":
        print(word,"\twrite\tIrregular")
