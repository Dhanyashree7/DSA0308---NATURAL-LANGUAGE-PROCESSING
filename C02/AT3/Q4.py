def parser(word):

    irregular = {
        "children": "child",
        "men": "man",
        "women": "woman",
        "mice": "mouse",
        "teeth": "tooth",
        "feet": "foot"
    }

    # Irregular plurals
    if word in irregular:
        return irregular[word], "Plural Noun (Irregular)"

    # Words ending in -ies
    elif word.endswith("ies"):
        return word[:-3] + "y", "Plural Noun (-ies)"

    # Words ending in -es
    elif word.endswith("es"):
        return word[:-2], "Plural Noun (-es)"

    # Regular plural ending in -s
    elif word.endswith("s"):
        return word[:-1], "Plural Noun (-s)"

    # Otherwise singular
    else:
        return word, "Singular"


words = [
    "cars",
    "boxes",
    "cities",
    "children",
    "books"
]

print("FINITE-STATE MORPHOLOGICAL PARSER")
print("=" * 60)

for w in words:
    root, category = parser(w)
    print(w, "->", root, "->", category)
