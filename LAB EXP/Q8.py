training = {
    "The":"DT",
    "cat":"NN",
    "drinks":"VBZ",
    "milk":"NN",
    "boy":"NN",
    "eats":"VBZ"
}

sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nPOS Tags")

for word in words:

    if word in training:
        print(word,"->",training[word])

    else:
        print(word,"->","NN")
