sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nPOS Tags")

for word in words:

    tag = "NN"

    if word.lower() in ["the","a","an"]:
        tag = "DT"

    if word.endswith("ing"):
        tag = "VBG"

    if word.endswith("ed"):
        tag = "VBD"

    if word.endswith("ly"):
        tag = "RB"

    print(word,"->",tag)
