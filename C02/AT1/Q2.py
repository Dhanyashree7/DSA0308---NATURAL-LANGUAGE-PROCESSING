words = ["unhappy", "happiness", "happily"]
print("Word\t\tPrefix\tRoot\tSuffix\tType")
for word in words:
    if word.startswith("un"):
        print(word,"\tun\thappy\t-\tDerivational")
    elif word.endswith("ness"):
        print(word,"\t-\thappy\tness\tDerivational")
    elif word.endswith("ly"):
        print(word,"\t-\thappy\tly\tDerivational")
