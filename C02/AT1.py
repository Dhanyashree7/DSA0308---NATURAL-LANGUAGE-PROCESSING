corpus = [
    ("the", "DT"),
    ("cat", "NN"),
    ("sat", "VBD"),
    ("the", "DT"),
    ("dog", "NN"),
    ("ran", "VBD"),
    ("the", "DT"),
    ("cat", "NN")
]
tags = {}
words = {}
for word, tag in corpus:
    if tag not in tags:
        tags[tag] = 0
    if (word, tag) not in words:
        words[(word, tag)] = 0
    tags[tag] += 1
    words[(word, tag)] += 1
print("Tag Counts:")
print(tags)
print("\nWord-Tag Counts:")
print(words)
print("\nProbabilities P(word|tag):")
for key in words:
    word, tag = key
    probability = words[key] / tags[tag]
    print(f"P({word}|{tag}) = {words[key]}/{tags[tag]} = {probability:.2f}")
