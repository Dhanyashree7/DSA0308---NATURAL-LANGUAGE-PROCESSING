text = "I love natural language processing and I love python"
words = text.split()
bigrams = []

for i in range(len(words) - 1):
    bigrams.append((words[i], words[i + 1]))

print("Bigrams:")
print(bigrams)
word = "I"

print("\nGenerated Text:")
print(word, end=" ")

for first, second in bigrams:
    if first == word:
        print(second, end=" ")
        word = second
