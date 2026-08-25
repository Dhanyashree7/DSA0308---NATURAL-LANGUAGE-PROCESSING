import nltk
from nltk.corpus import wordnet

nltk.download("wordnet")

word = input("Enter word: ")
sentence = input("Enter sentence: ")

synsets = wordnet.synsets(word)

best = None
max_match = 0

for syn in synsets:
    definition = syn.definition().lower()
    count = 0

    for w in sentence.lower().split():
        if w in definition:
            count += 1

    if count > max_match:
        max_match = count
        best = syn

if best:
    print("Best Sense:", best.name())
    print("Meaning:", best.definition())
else:
    print("Sense not found")
