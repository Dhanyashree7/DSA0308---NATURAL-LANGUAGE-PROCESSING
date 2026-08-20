words = [
    "treatment",
    "treatable",
    "retreatment",
    "treated",
    "untreated"
]

analysis = {
    "treatment": {
        "prefix": "-",
        "root": "treat",
        "suffix": "ment",
        "type": "Derivational"
    },

    "treatable": {
        "prefix": "-",
        "root": "treat",
        "suffix": "able",
        "type": "Derivational"
    },

    "retreatment": {
        "prefix": "re",
        "root": "treat",
        "suffix": "ment",
        "type": "Derivational + Derivational"
    },

    "treated": {
        "prefix": "-",
        "root": "treat",
        "suffix": "ed",
        "type": "Inflectional"
    },

    "untreated": {
        "prefix": "un",
        "root": "treat",
        "suffix": "ed",
        "type": "Derivational + Inflectional"
    }
}

print("Corrected Morphological Analysis")
print("-" * 60)

for word in words:
    data = analysis[word]

    print("\nWord:", word)
    print("Prefix:", data["prefix"])
    print("Root:", data["root"])
    print("Suffix:", data["suffix"])
    print("Affix Type:", data["type"])
