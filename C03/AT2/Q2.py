from collections import Counter
import re

corpus = """
Machine learning can analyze data.
Machine learning can solve problems.
Machine learning is a part of artificial intelligence.
Artificial intelligence can solve complex problems.
Artificial intelligence can analyze large amounts of data.
Deep learning can solve complex problems.
Deep learning is a branch of machine learning.
Natural language processing can understand human language.
Natural language processing is used in many applications.
Computers can learn from data.
Computers can understand human language.
Data science can help organizations make decisions.
Data science uses machine learning techniques.
Technology can help people learn.
Technology can change the way people work.
Machine learning helps computers learn from data.
"""

# ============================================================
# TOKENIZATION
# ============================================================

sentences = re.split(r'[.!?]+', corpus.lower())

tokenized_sentences = []

for sentence in sentences:
    words = re.findall(r'\b[a-z]+\b', sentence)

    if words:
        tokenized_sentences.append(words)


# ============================================================
# N-GRAM COUNTS
# ============================================================

unigram = Counter()
bigram = Counter()
trigram = Counter()

for words in tokenized_sentences:

    unigram.update(words)

    for i in range(len(words) - 1):
        bigram[(words[i], words[i + 1])] += 1

    for i in range(len(words) - 2):
        trigram[
            (words[i], words[i + 1], words[i + 2])
        ] += 1


total_words = sum(unigram.values())


# ============================================================
# PROBABILITY FUNCTIONS
# ============================================================

def unigram_probability(word):

    return unigram[word] / total_words


def bigram_probability(previous, word):

    denominator = unigram[previous]

    if denominator == 0:
        return 0

    return bigram[(previous, word)] / denominator


def trigram_probability(previous1, previous2, word):

    denominator = bigram[(previous1, previous2)]

    if denominator == 0:
        return 0

    return trigram[
        (previous1, previous2, word)
    ] / denominator


# ============================================================
# UNSMOOTHED TRIGRAM MODEL
# ============================================================

def unsmoothed_prediction(sentence):

    words = re.findall(r'\b[a-z]+\b', sentence.lower())

    if len(words) < 2:
        return []

    previous1 = words[-2]
    previous2 = words[-1]

    predictions = []

    for word in unigram:

        probability = trigram_probability(
            previous1,
            previous2,
            word
        )

        if probability > 0:
            predictions.append(
                (word, probability)
            )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# ============================================================
# BACKOFF MODEL
# ============================================================

def backoff_probability(previous1, previous2, word):

    # First check trigram
    trigram_prob = trigram_probability(
        previous1,
        previous2,
        word
    )

    if trigram_prob > 0:
        return trigram_prob, "Trigram"

    # Then check bigram
    bigram_prob = bigram_probability(
        previous2,
        word
    )

    if bigram_prob > 0:
        return bigram_prob, "Bigram"

    # Finally use unigram
    unigram_prob = unigram_probability(word)

    return unigram_prob, "Unigram"


def backoff_prediction(sentence):

    words = re.findall(r'\b[a-z]+\b', sentence.lower())

    if len(words) < 2:
        return []

    previous1 = words[-2]
    previous2 = words[-1]

    predictions = []

    for word in unigram:

        probability, source = backoff_probability(
            previous1,
            previous2,
            word
        )

        predictions.append(
            (word, probability, source)
        )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# ============================================================
# DELETED INTERPOLATION MODEL
# ============================================================

lambda1 = 0.2
lambda2 = 0.3
lambda3 = 0.5


def interpolation_probability(
    previous1,
    previous2,
    word
):

    p1 = unigram_probability(word)

    p2 = bigram_probability(
        previous2,
        word
    )

    p3 = trigram_probability(
        previous1,
        previous2,
        word
    )

    probability = (
        lambda1 * p1 +
        lambda2 * p2 +
        lambda3 * p3
    )

    return probability


def interpolation_prediction(sentence):

    words = re.findall(
        r'\b[a-z]+\b',
        sentence.lower()
    )

    if len(words) < 2:
        return []

    previous1 = words[-2]
    previous2 = words[-1]

    predictions = []

    for word in unigram:

        probability = interpolation_probability(
            previous1,
            previous2,
            word
        )

        predictions.append(
            (word, probability)
        )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# ============================================================
# DISPLAY PREDICTIONS
# ============================================================

def display_predictions(sentence):

    print("\n" + "=" * 70)
    print("INPUT:", sentence)
    print("=" * 70)

    # ---------------- UNSMOOTHED ----------------

    print("\n1. UNSMOOTHED TRIGRAM MODEL")
    print("-" * 70)

    result = unsmoothed_prediction(sentence)

    if result:

        for word, probability in result:
            print(
                f"{word:15} {probability:.4f}"
            )

    else:
        print(
            "No trigram found."
        )
        print(
            "Probability = 0"
        )

    # ---------------- BACKOFF ----------------

    print("\n2. BACKOFF MODEL")
    print("-" * 70)

    result = backoff_prediction(sentence)

    for word, probability, source in result:

        print(
            f"{word:15} {probability:.4f}"
            f"   Source: {source}"
        )

    # ---------------- INTERPOLATION ----------------

    print("\n3. DELETED INTERPOLATION MODEL")
    print("-" * 70)

    result = interpolation_prediction(sentence)

    for word, probability in result:

        print(
            f"{word:15} {probability:.4f}"
        )


# ============================================================
# USER INPUT
# ============================================================

print("=" * 70)
print("BACKOFF AND INTERPOLATION LANGUAGE PREDICTION")
print("=" * 70)

sentence = input(
    "\nEnter an incomplete sentence: "
)

display_predictions(sentence)


# ============================================================
# TEST CASES
# ============================================================

print("\n\n" + "=" * 70)
print("MODEL EVALUATION")
print("=" * 70)

test_cases = [
    ("machine learning can", "analyze"),
    ("deep learning can", "solve"),
    ("artificial intelligence can", "solve"),
    ("natural language processing can", "understand")
]

unsmoothed_correct = 0
backoff_correct = 0
interpolation_correct = 0

for sentence, expected in test_cases:

    print("\nSentence:", sentence)
    print("Expected word:", expected)

    # Unsmoothed
    unsmoothed = unsmoothed_prediction(sentence)

    unsmoothed_words = [
        word for word, probability in unsmoothed
    ]

    if expected in unsmoothed_words:
        unsmoothed_correct += 1

    # Backoff
    backoff = backoff_prediction(sentence)

    backoff_words = [
        word for word, probability, source in backoff
    ]

    if expected in backoff_words:
        backoff_correct += 1

    # Interpolation
    interpolation = interpolation_prediction(sentence)

    interpolation_words = [
        word for word, probability in interpolation
    ]

    if expected in interpolation_words:
        interpolation_correct += 1


total = len(test_cases)

unsmoothed_accuracy = (
    unsmoothed_correct / total
) * 100

backoff_accuracy = (
    backoff_correct / total
) * 100

interpolation_accuracy = (
    interpolation_correct / total
) * 100


# ============================================================
# FINAL COMPARISON
# ============================================================

print("\n" + "=" * 70)
print("FINAL COMPARISON")
print("=" * 70)

print(
    f"\nUnsmoothed Accuracy     : "
    f"{unsmoothed_accuracy:.2f}%"
)

print(
    f"Backoff Accuracy       : "
    f"{backoff_accuracy:.2f}%"
)

print(
    f"Interpolation Accuracy : "
    f"{interpolation_accuracy:.2f}%"
)


print("\nMODEL CHARACTERISTICS")
print("-" * 70)

print("""
Unsmoothed Model:
- Uses only observed trigrams.
- Unseen trigrams get probability zero.
- Low prediction coverage.

Backoff Model:
- Uses trigram first.
- If unavailable, uses bigram.
- If unavailable, uses unigram.
- Provides better prediction coverage.

Interpolation Model:
- Combines unigram, bigram and trigram probabilities.
- Reduces the effect of zero probabilities.
- Provides smoother predictions.
""")
