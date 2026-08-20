from collections import Counter, defaultdict
import re

training_data = [
    [
        ("i", "PRP"),
        ("book", "VB"),
        ("a", "DT"),
        ("ticket", "NN")
    ],

    [
        ("i", "PRP"),
        ("read", "VB"),
        ("a", "DT"),
        ("book", "NN")
    ],

    [
        ("the", "DT"),
        ("cat", "NN"),
        ("sits", "VBZ"),
        ("on", "IN"),
        ("the", "DT"),
        ("mat", "NN")
    ],

    [
        ("the", "DT"),
        ("dog", "NN"),
        ("runs", "VBZ"),
        ("quickly", "RB")
    ],

    [
        ("the", "DT"),
        ("boy", "NN"),
        ("plays", "VBZ"),
        ("with", "IN"),
        ("the", "DT"),
        ("ball", "NN")
    ],

    [
        ("the", "DT"),
        ("girl", "NN"),
        ("reads", "VBZ"),
        ("a", "DT"),
        ("book", "NN")
    ],

    [
        ("students", "NNS"),
        ("study", "VB"),
        ("computer", "NN"),
        ("science", "NN")
    ],

    [
        ("machines", "NNS"),
        ("learn", "VB"),
        ("from", "IN"),
        ("data", "NNS")
    ]
]


# ============================================================
# BUILD WORD/TAG FREQUENCIES
# ============================================================

word_tag_counts = defaultdict(Counter)
tag_counts = Counter()
transition_counts = defaultdict(Counter)

for sentence in training_data:

    previous_tag = "<START>"

    for word, tag in sentence:

        word_tag_counts[word][tag] += 1
        tag_counts[tag] += 1

        transition_counts[previous_tag][tag] += 1

        previous_tag = tag


# ============================================================
# LEXICAL DICTIONARY
# ============================================================

lexicon = {}

for word in word_tag_counts:

    lexicon[word] = (
        word_tag_counts[word]
        .most_common(1)[0][0]
    )


# ============================================================
# TOKENIZATION
# ============================================================

def tokenize(sentence):

    return re.findall(
        r'\b[a-zA-Z]+\b',
        sentence.lower()
    )


# ============================================================
# RULE-BASED TAGGER
# ============================================================

def rule_based_tag(words):

    tags = []

    for word in words:

        # Known words
        if word in lexicon:

            tag = lexicon[word]

        # Determiners
        elif word in ["a", "an", "the"]:

            tag = "DT"

        # Pronouns
        elif word in [
            "i", "you", "he", "she",
            "we", "they", "it"
        ]:

            tag = "PRP"

        # Prepositions
        elif word in [
            "in", "on", "at",
            "with", "from",
            "to", "for"
        ]:

            tag = "IN"

        # Adverbs
        elif word.endswith("ly"):

            tag = "RB"

        # Verbs ending with common forms
        elif word.endswith(
            ("ing", "ed")
        ):

            tag = "VBG"

        # Plural nouns
        elif word.endswith("s"):

            tag = "NNS"

        else:

            tag = "NN"

        tags.append((word, tag))

    return tags


# ============================================================
# STOCHASTIC POS TAGGER
# ============================================================

def stochastic_tag(words):

    result = []

    previous_tag = "<START>"

    all_tags = list(tag_counts.keys())

    for word in words:

        best_tag = None
        best_probability = 0

        for tag in all_tags:

            # Word probability
            word_count = word_tag_counts[word][tag]

            total_word_count = sum(
                word_tag_counts[word].values()
            )

            if total_word_count > 0:

                emission = (
                    word_count /
                    total_word_count
                )

            else:

                emission = 1 / len(all_tags)

            # Transition probability
            previous_total = sum(
                transition_counts[
                    previous_tag
                ].values()
            )

            if previous_total > 0:

                transition = (
                    transition_counts[
                        previous_tag
                    ][tag] /
                    previous_total
                )

            else:

                transition = 1 / len(all_tags)

            probability = (
                emission * transition
            )

            if probability > best_probability:

                best_probability = probability
                best_tag = tag

        # Unknown word handling
        if word not in word_tag_counts:

            if word.endswith("ly"):
                best_tag = "RB"

            elif word.endswith("s"):
                best_tag = "NNS"

            elif word.endswith("ing"):
                best_tag = "VBG"

            else:
                best_tag = "NN"

        result.append(
            (word, best_tag)
        )

        previous_tag = best_tag

    return result


# ============================================================
# TRANSFORMATION-BASED TAGGER
# ============================================================

def transformation_based_tag(words):

    # Initial tagging using rule-based tagger

    tagged = rule_based_tag(words)

    # Transformation 1:
    # "book" after determiner -> noun
    for i in range(len(tagged)):

        word, tag = tagged[i]

        if (
            word == "book"
            and i > 0
            and tagged[i - 1][1] == "DT"
        ):

            tagged[i] = (word, "NN")

    # Transformation 2:
    # "book" after pronoun -> verb
    for i in range(len(tagged)):

        word, tag = tagged[i]

        if (
            word == "book"
            and i > 0
            and tagged[i - 1][1] == "PRP"
        ):

            tagged[i] = (word, "VB")

    # Transformation 3:
    # Words ending in ly -> adverb
    for i in range(len(tagged)):

        word, tag = tagged[i]

        if word.endswith("ly"):

            tagged[i] = (word, "RB")

    return tagged


# ============================================================
# DISPLAY
# ============================================================

def display_tags(title, tagged_words):

    print("\n" + title)
    print("-" * 60)

    for word, tag in tagged_words:

        print(
            f"{word:15} -> {tag}"
        )


# ============================================================
# USER INPUT
# ============================================================

print("=" * 70)
print("COMPARATIVE POS TAGGING SYSTEM")
print("=" * 70)

sentence = input(
    "\nEnter an English sentence: "
)

words = tokenize(sentence)


# Rule-Based
rule_result = rule_based_tag(words)

# Stochastic
stochastic_result = stochastic_tag(words)

# Transformation-Based
transformation_result = (
    transformation_based_tag(words)
)


# ============================================================
# DISPLAY RESULTS
# ============================================================

display_tags(
    "1. RULE-BASED POS TAGGING",
    rule_result
)

display_tags(
    "2. STOCHASTIC POS TAGGING",
    stochastic_result
)

display_tags(
    "3. TRANSFORMATION-BASED POS TAGGING",
    transformation_result
)


# ============================================================
# DEMONSTRATION OF CONTEXT
# ============================================================

print("\n" + "=" * 70)
print("CONTEXT SENSITIVITY DEMONSTRATION")
print("=" * 70)

sentences = [
    "I book a ticket.",
    "I read a book."
]

for example in sentences:

    words = tokenize(example)

    result = transformation_based_tag(
        words
    )

    print("\nSentence:", example)

    for word, tag in result:

        if word == "book":

            print(
                "book ->",
                tag
            )


# ============================================================
# ACCURACY EVALUATION
# ============================================================

test_data = [
    (
        ["i", "book", "a", "ticket"],
        ["PRP", "VB", "DT", "NN"]
    ),

    (
        ["i", "read", "a", "book"],
        ["PRP", "VB", "DT", "NN"]
    ),

    (
        ["the", "cat", "sits", "on", "the", "mat"],
        ["DT", "NN", "VBZ", "IN", "DT", "NN"]
    )
]


def calculate_accuracy(
    tagger
):

    correct = 0
    total = 0

    for words, expected in test_data:

        result = tagger(words)

        predicted = [
            tag for word, tag in result
        ]

        for p, e in zip(
            predicted,
            expected
        ):

            if p == e:
                correct += 1

            total += 1

    return (
        correct / total
    ) * 100


rule_accuracy = calculate_accuracy(
    rule_based_tag
)

stochastic_accuracy = calculate_accuracy(
    stochastic_tag
)

transformation_accuracy = calculate_accuracy(
    transformation_based_tag
)


# ============================================================
# FINAL COMPARISON
# ============================================================

print("\n" + "=" * 70)
print("ACCURACY COMPARISON")
print("=" * 70)

print(
    f"\nRule-Based Accuracy          : "
    f"{rule_accuracy:.2f}%"
)

print(
    f"Stochastic Accuracy         : "
    f"{stochastic_accuracy:.2f}%"
)

print(
    f"Transformation-Based Accuracy: "
    f"{transformation_accuracy:.2f}%"
)


# ============================================================
# ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("ANALYSIS")
print("=" * 70)

print("""
Rule-Based Tagging:
Uses dictionaries, word patterns and grammatical rules.
It is simple and easy to understand but depends on manually
defined rules.

Stochastic Tagging:
Uses word/tag frequencies and tag transition probabilities.
It is data-driven but requires a tagged training corpus.

Transformation-Based Tagging:
Starts with an initial tagging and applies transformation
rules to correct errors. It can improve context-sensitive
tagging.

Example:
"I book a ticket." -> book = VB
"I read a book."    -> book = NN
""")
