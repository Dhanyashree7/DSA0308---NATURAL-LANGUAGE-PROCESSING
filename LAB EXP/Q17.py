import nltk
from nltk.corpus import wordnet
nltk.download("wordnet")
word = input("Enter a word: ")
synsets = wordnet.synsets(word)
for syn in synsets:
    print("Synset:", syn.name())
    print("Meaning:", syn.definition())
    print()
