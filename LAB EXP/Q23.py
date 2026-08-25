text = input("Enter text: ")

sentences = text.split(".")

previous_words = set()

score = 0

for sentence in sentences:

    words = set(sentence.lower().split())

    common = previous_words.intersection(words)

    if len(common) > 0:
        score = score + 1

    previous_words = words

print("Coherence Score:", score)

if score > 0:
    print("Text is Coherent")
else:
    print("Text has Low Coherence")
