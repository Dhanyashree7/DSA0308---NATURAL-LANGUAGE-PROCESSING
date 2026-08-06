# Simple Top-Down Parser

grammar = {
    "S": ["NP VP"],
    "NP": ["Det N"],
    "VP": ["V NP"],
    "Det": ["the", "a"],
    "N": ["boy", "girl", "apple"],
    "V": ["eats", "likes"]
}

sentence = input("Enter a sentence: ").lower().split()

# Expected pattern:
# S -> NP VP
# NP -> Det N
# VP -> V NP

if len(sentence) == 5:
    if (sentence[0] in grammar["Det"] and
        sentence[1] in grammar["N"] and
        sentence[2] in grammar["V"] and
        sentence[3] in grammar["Det"] and
        sentence[4] in grammar["N"]):

        print("\nSentence Accepted")
        print("Parse Tree")
        print("S")
        print("|-- NP")
        print("|   |-- Det :", sentence[0])
        print("|   |-- N   :", sentence[1])
        print("|-- VP")
        print("    |-- V   :", sentence[2])
        print("    |-- NP")
        print("        |-- Det :", sentence[3])
        print("        |-- N   :", sentence[4])

    else:
        print("\nSentence Rejected")

else:
    print("\nSentence Rejected")
