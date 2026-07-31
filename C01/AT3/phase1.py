def step1a(word):
    if word.endswith("ss"):
        return word
    return word
word = input("Enter word:")
print("original word:",word)
print("after step 1a rule 3:",step1a(word))