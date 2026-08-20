from collections import Counter
import re
import math

training_corpus = """
The cat sits on the mat.
The cat eats the food.
The cat likes the mat.
The dog sits on the mat.
The dog eats the food.
The dog likes the food.
The boy plays with the ball.
The girl plays with the ball.
The boy likes the dog.
The girl likes the cat.
Machine learning is a part of artificial intelligence.
Machine learning can analyze data.
Artificial intelligence can solve problems.
Natural language processing understands human language.
The computer learns from data.
"""


# ------------------------------------------------------------
# TESTING CORPUS
# ------------------------------------------------------------

test_sentences = [
    "The cat sits on the mat.",
    "The quantum processor redesigned the system."
]


# ------------------------------------------------------------
# TOKENIZATION
# ------------------------------------------------------------

def tokenize(text):
    return re.findall(
        r'\b[a-z]+\b',
        text.lower()
    )


train_tokens = tokenize(training_corpus)


# ------------------------------------------------------------
# N-GRAM COUNTS
# ------------------------------------------------------------

unigram = Counter(train_tokens)

bigram = Counter()

trigram = Counter()

for i in range(len(train_tokens) - 1):
    bigram[
        (train_tokens[i], train_tokens[i + 1])
    ] += 1

for i in range(len(train_tokens) - 2):
    trigram[
        (
            train_tokens[i],
            train_tokens[i + 1],
            train_tokens[i + 2]
        )
    ] += 1


vocabulary = set(train_tokens)

V = len(vocabulary)

total_words = len(train_tokens)


# ------------------------------------------------------------
# UNIGRAM PROBABILITY
# ------------------------------------------------------------

def unigram_probability(word):

    return unigram[word] / total_words


# ------------------------------------------------------------
# BIGRAM PROBABILITY
# ------------------------------------------------------------

def bigram_probability(previous, word):

    denominator = unigram[previous]

    if denominator == 0:
        return 0

    return bigram[
        (previous, word)
    ] / denominator


# ------------------------------------------------------------
# TRIGRAM PROBABILITY
# ------------------------------------------------------------

def trigram_probability(
    previous1,
    previous2,
    word
):

    denominator = bigram[
        (previous1, previous2)
    ]

    if denominator == 0:
        return 0

    return trigram[
        (previous1, previous2, word)
    ] / denominator


# ------------------------------------------------------------
# SMOOTHED UNIGRAM
# ------------------------------------------------------------

def smoothed_unigram_probability(word):

    return (
        unigram[word] + 1
    ) / (
        total_words + V
    )


# ------------------------------------------------------------
# SMOOTHED BIGRAM
# ------------------------------------------------------------

def smoothed_bigram_probability(
    previous,
    word
):

    return (
        bigram[(previous, word)] + 1
    ) / (
        unigram[previous] + V
    )


# ------------------------------------------------------------
# SMOOTHED TRIGRAM
# ------------------------------------------------------------

def smoothed_trigram_probability(
    previous1,
    previous2,
    word
):

    return (
        trigram[
            (previous1, previous2, word)
        ] + 1
    ) / (
        bigram[
            (previous1, previous2)
        ] + V
    )


# ------------------------------------------------------------
# ENTROPY CALCULATION
# ------------------------------------------------------------

def calculate_entropy(probabilities):

    entropy = 0

    for probability in probabilities:

        if probability > 0:
            entropy += -math.log2(probability)

    if len(probabilities) == 0:
        return 0

    return entropy / len(probabilities)


# ------------------------------------------------------------
# UNIGRAM ENTROPY
# ------------------------------------------------------------

def unigram_entropy(words):

    probabilities = []

    for word in words:

        probability = unigram_probability(
            word
        )

        probabilities.append(probability)

    return calculate_entropy(probabilities)


# ------------------------------------------------------------
# BIGRAM ENTROPY
# ------------------------------------------------------------

def bigram_entropy(words):

    probabilities = []

    for i in range(1, len(words)):

        probability = bigram_probability(
            words[i - 1],
            words[i]
        )

        if probability > 0:
            probabilities.append(probability)

    return calculate_entropy(probabilities)


# ------------------------------------------------------------
# TRIGRAM ENTROPY
# ------------------------------------------------------------

def trigram_entropy(words):

    probabilities = []

    for i in range(2, len(words)):

        probability = trigram_probability(
            words[i - 2],
            words[i - 1],
            words[i]
        )

        if probability > 0:
            probabilities.append(probability)

    return calculate_entropy(probabilities)


# ------------------------------------------------------------
# SMOOTHED TRIGRAM ENTROPY
# ------------------------------------------------------------

def smoothed_trigram_entropy(words):

    probabilities = []

    for i in range(2, len(words)):

        probability = smoothed_trigram_probability(
            words[i - 2],
            words[i - 1],
            words[i]
        )

        probabilities.append(probability)

    return calculate_entropy(probabilities)


# ------------------------------------------------------------
# UNCERTAINTY CLASSIFICATION
# ------------------------------------------------------------

def classify(entropy):

    if entropy < 3:
        return "Low Predictive Uncertainty"
    else:
        return "High Predictive Uncertainty"


# ============================================================
# MAIN PROGRAM
# ============================================================

print("=" * 70)
print("ENTROPY-BASED LANGUAGE MODEL EVALUATION")
print("=" * 70)

print("\nTraining Corpus Words:", total_words)
print("Vocabulary Size:", V)


for sentence in test_sentences:

    words = tokenize(sentence)

    print("\n" + "=" * 70)
    print("TEST SENTENCE:")
    print(sentence)
    print("=" * 70)

    # Unigram
    uni_entropy = unigram_entropy(words)

    # Bigram
    bi_entropy = bigram_entropy(words)

    # Trigram
    tri_entropy = trigram_entropy(words)

    # Smoothed trigram
    smooth_entropy = smoothed_trigram_entropy(words)

    print("\nEntropy Results")
    print("-" * 70)

    print(
        f"Unigram Entropy       : "
        f"{uni_entropy:.4f}"
    )

    print(
        f"Bigram Entropy        : "
        f"{bi_entropy:.4f}"
    )

    print(
        f"Trigram Entropy       : "
        f"{tri_entropy:.4f}"
    )

    print(
        f"Smoothed Trigram     : "
        f"{smooth_entropy:.4f}"
    )

    print("\nPredictive Uncertainty")
    print("-" * 70)

    print(
        "Unigram  :",
        classify(uni_entropy)
    )

    print(
        "Bigram   :",
        classify(bi_entropy)
    )

    print(
        "Trigram  :",
        classify(tri_entropy)
    )

    print(
        "Smoothed :",
        classify(smooth_entropy)
    )


# ============================================================
# COMPARISON
# ============================================================

print("\n\n" + "=" * 70)
print("INTERPRETATION")
print("=" * 70)

print("""
Low entropy means that the language model finds the
sentence relatively predictable.

High entropy means that the model is uncertain about
the words appearing in the sentence.

Unigram model:
Uses only individual word frequencies.

Bigram model:
Uses the previous word as context.

Trigram model:
Uses the previous two words as context.

Smoothed model:
Assigns non-zero probability to unseen N-grams
and reduces the zero-probability problem.
""")
