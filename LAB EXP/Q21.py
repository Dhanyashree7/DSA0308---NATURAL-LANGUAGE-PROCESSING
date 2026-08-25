import nltk
from nltk.corpus import wordnet

nltk.download("wordnet")

sentence = input("Enter sentence: ")

words = sentence.lower().split()

print("\nNoun Phrases and Meanings:")

for word in words:

    synsets = wordnet.synsets(word, pos=wordnet.NOUN)

    if synsets:
        print("Noun:", word)
        print("Meaning:", synsets[0].definition())
        print()
