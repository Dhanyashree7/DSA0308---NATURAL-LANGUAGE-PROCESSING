from collections import Counter
import re


corpus = """
Artificial intelligence is transforming the world.
Artificial intelligence is changing modern technology.
Artificial intelligence helps people solve complex problems.
Machine learning is a part of artificial intelligence.
Machine learning can analyze large amounts of data.
Machine learning helps computers learn from data.
Deep learning is a branch of machine learning.
Deep learning can solve complex problems.
Natural language processing helps computers understand language.
Natural language processing is used in many applications.
Computers can understand human language.
Computers can learn from large amounts of data.
Data science helps organizations make better decisions.
Data science uses machine learning techniques.
Technology is changing the way people work.
Technology helps people communicate and learn.
"""

# --------------------------------------------------
# TOKENIZATION
# --------------------------------------------------

sentences = re.split(r'[.!?]+', corpus.lower())

tokenized_sentences = []

for sentence in sentences:
    words = re.findall(r'\b[a-z]+\b', sentence)

    if words:
        tokenized_sentences.append(words)


# --------------------------------------------------
# CREATE N-GRAM COUNTS
# --------------------------------------------------

unigram_counts = Counter()
bigram_counts = Counter()
trigram_counts = Counter()

for words in tokenized_sentences:

    unigram_counts.update(words)

    for i in range(len(words) - 1):
        bigram_counts[(words[i], words[i + 1])] += 1

    for i in range(len(words) - 2):
        trigram_counts[
            (words[i], words[i + 1], words[i + 2])
        ] += 1


# --------------------------------------------------
# PROBABILITY FUNCTIONS
# --------------------------------------------------

def unigram_probability(word):
    total = sum(unigram_counts.values())

    return unigram_counts[word] / total


def bigram_probability(word, previous):
    count = bigram_counts[(previous, word)]

    if unigram_counts[previous] == 0:
        return 0

    return count / unigram_counts[previous]


def trigram_probability(word, previous1, previous2):
    count = trigram_counts[(previous1, previous2, word)]

    denominator = bigram_counts[(previous1, previous2)]

    if denominator == 0:
        return 0

    return count / denominator


# --------------------------------------------------
# NEXT WORD PREDICTION
# --------------------------------------------------

def predict_next_words(sentence, n):

    words = re.findall(r'\b[a-z]+\b', sentence.lower())

    candidates = []

    if n == 1:

        for word in unigram_counts:
            probability = unigram_probability(word)
            candidates.append((word, probability))

    elif n == 2:

        if len(words) < 1:
            return []

        previous = words[-1]

        for word in unigram_counts:
            probability = bigram_probability(word, previous)

            if probability > 0:
                candidates.append((word, probability))

    elif n == 3:

        if len(words) < 2:
            return []

        previous1 = words[-2]
        previous2 = words[-1]

        for word in unigram_counts:
            probability = trigram_probability(
                word,
                previous1,
                previous2
            )

            if probability > 0:
                candidates.append((word, probability))

    candidates.sort(key=lambda x: x[1], reverse=True)

    return candidates[:5]


# --------------------------------------------------
# DISPLAY N-GRAM COUNTS
# --------------------------------------------------

print("=" * 70)
print("N-GRAM LANGUAGE MODEL")
print("=" * 70)

print("\nUNIGRAM COUNTS")
print("-" * 70)

for word, count in unigram_counts.most_common(15):
    print(word, ":", count)


print("\nBIGRAM COUNTS")
print("-" * 70)

for pair, count in bigram_counts.most_common(15):
    print(pair, ":", count)


print("\nTRIGRAM COUNTS")
print("-" * 70)

for triple, count in trigram_counts.most_common(15):
    print(triple, ":", count)


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

print("\n" + "=" * 70)

sentence = input(
    "Enter an incomplete sentence: "
)

n = int(input(
    "Select N (1 = Unigram, 2 = Bigram, 3 = Trigram): "
))

predictions = predict_next_words(sentence, n)


print("\nTOP-5 NEXT WORD PREDICTIONS")
print("-" * 70)

if predictions:

    for word, probability in predictions:
        print(
            f"{word:15} Probability = {probability:.4f}"
        )

else:

    print(
        "No matching N-gram found."
    )

    print(
        "The N-gram is unseen and has probability 0."
    )


# --------------------------------------------------
# TEST CASES
# --------------------------------------------------

print("\n" + "=" * 70)
print("TEST CASES")
print("=" * 70)

test_cases = [
    ("artificial intelligence is", "transforming"),
    ("machine learning is", "a"),
    ("natural language processing is", "used"),
    ("deep learning is", "a")
]

correct = 0

for sentence, expected in test_cases:

    predictions = predict_next_words(sentence, 3)

    predicted_words = [
        word for word, probability in predictions
    ]

    if expected in predicted_words:
        correct += 1
        result = "Correct"
    else:
        result = "Incorrect"

    print("\nSentence:", sentence)
    print("Expected:", expected)
    print("Predicted:", predicted_words)
    print("Result:", result)


accuracy = (correct / len(test_cases)) * 100

print("\nPrediction Accuracy:",
      round(accuracy, 2), "%")


# --------------------------------------------------
# UNSEEN N-GRAM DEMONSTRATION
# --------------------------------------------------

print("\n" + "=" * 70)
print("UNSEEN N-GRAM DEMONSTRATION")
print("=" * 70)

unseen_sentence = "quantum processor"

predictions = predict_next_words(
    unseen_sentence,
    3
)

if not predictions:

    print(
        "No trigram found for:",
        unseen_sentence
    )

    print(
        "Probability = 0"
    )

    print(
        "This demonstrates the zero-probability problem "
        "of an unsmoothed N-gram model."
    )


# --------------------------------------------------
# LIMITATIONS
# --------------------------------------------------

print("\n" + "=" * 70)
print("LIMITATIONS")
print("=" * 70)

print("""
1. Unseen N-grams receive probability zero.
2. The model depends heavily on the training corpus.
3. Long-range word relationships are not captured.
4. Vocabulary size can become very large.
5. Rare words may have unreliable probabilities.
6. No smoothing is applied.
7. Prediction accuracy decreases for unseen contexts.
""")
