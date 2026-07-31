# Porter Stemmer - Step 3

def step3(word):

    if word.endswith("icate"):
        return word[:-5] + "ic"

    elif word.endswith("ative"):
        return word[:-5]

    elif word.endswith("alize"):
        return word[:-5] + "al"

    elif word.endswith("iciti"):
        return word[:-5] + "ic"

    elif word.endswith("ical"):
        return word[:-4] + "ic"

    elif word.endswith("ful"):
        return word[:-3]

    elif word.endswith("ness"):
        return word[:-4]

    else:
        return word


words = [
    "triplicate",
    "formative",
    "formalize",
    "electricity",
    "electrical",
    "hopeful",
    "kindness",
    "computer",
    "running",
    "table"
]

print("Original Word\t\tStemmed Word")
print("---------------------------------------")

for word in words:
    print(f"{word:15}\t{step3(word)}")
