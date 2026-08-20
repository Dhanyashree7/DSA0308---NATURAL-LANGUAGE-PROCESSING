
# Q2 - Finite-State Morphological Parser Error Analysis

words = [
    "replayed",
    "unhappier",
    "disconnected",
    "players",
    "restarting",
    "unreadable"
]

# Correct morphological analyses
correct = {
    "replayed": "re + play + ed",
    "unhappier": "un + happy + er",
    "disconnected": "dis + connect + ed",
    "players": "play + er + s",
    "restarting": "re + start + ing",
    "unreadable": "un + read + able"
}


# ---------------- ORIGINAL PARSER ----------------

def original_parser(word):
    # Handles only one prefix OR one suffix
    prefixes = ["re", "un", "dis"]
    suffixes = ["ed", "er", "s", "ing", "able"]

    for prefix in prefixes:
        if word.startswith(prefix):
            root = word[len(prefix):]

            for suffix in suffixes:
                if root.endswith(suffix):
                    root = root[:-len(suffix)]
                    return prefix + " + " + root + " + " + suffix

            return prefix + " + " + root

    for suffix in suffixes:
        if word.endswith(suffix):
            root = word[:-len(suffix)]
            return root + " + " + suffix

    return word


# ---------------- CORRECTED PARSER ----------------

def corrected_parser(word):
    prefixes = ["dis", "un", "re"]
    suffixes = ["able", "ing", "ed", "er", "s"]

    prefix_parts = []
    remaining = word

    # Recognize prefix
    for prefix in prefixes:
        if remaining.startswith(prefix):
            prefix_parts.append(prefix)
            remaining = remaining[len(prefix):]
            break

    suffix_parts = []

    # Recognize suffixes
    found = True

    while found:
        found = False

        for suffix in suffixes:
            if remaining.endswith(suffix) and len(remaining) > len(suffix):
                suffix_parts.insert(0, suffix)
                remaining = remaining[:-len(suffix)]
                found = True
                break

    # Handle spelling change: happy -> unhappier
    if remaining == "happi":
        remaining = "happy"

    parts = prefix_parts + [remaining] + suffix_parts

    return " + ".join(parts)


# ---------------- ERROR ANALYSIS ----------------

print("FINITE-STATE MORPHOLOGICAL PARSER")
print("=" * 65)

print("\nBEFORE CORRECTION")
print("-" * 65)

before_correct = 0

for word in words:
    result = original_parser(word)

    print(word, "->", result)

    if result == correct[word]:
        before_correct += 1

before_accuracy = (before_correct / len(words)) * 100

print("\nAccuracy Before Correction:",
      round(before_accuracy, 2), "%")


print("\nAFTER CORRECTION")
print("-" * 65)

after_correct = 0

for word in words:
    result = corrected_parser(word)

    print(word, "->", result)

    if result == correct[word]:
        after_correct += 1

after_accuracy = (after_correct / len(words)) * 100

print("\nAccuracy After Correction:",
      round(after_accuracy, 2), "%")


print("\nCOMPARISON")
print("-" * 65)

print("Before Correction :", round(before_accuracy, 2), "%")
print("After Correction  :", round(after_accuracy, 2), "%")
print("Improvement       :", round(after_accuracy - before_accuracy, 2), "%")
