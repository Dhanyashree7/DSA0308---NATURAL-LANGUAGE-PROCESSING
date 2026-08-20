import re
from nltk.stem import PorterStemmer

ps = PorterStemmer()

documents = [
    "The students are studying natural language processing.",
    "Researchers developed advanced machine learning models.",
    "The connected devices are connecting to the network.",
    "The organization organized several educational programs.",
    "Scientists are studying new treatments."
]

def preprocess(text):
    tokens = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    stems = [ps.stem(word) for word in tokens]
    return tokens, stems

print("STEMMING ERROR ANALYSIS")
print("=" * 60)

for text in documents:

    tokens, stems = preprocess(text)

    print("\nOriginal Text:")
    print(text)

    print("\nTokens:")
    print(tokens)

    print("\nStemmed Tokens:")
    print(stems)

    print("-" * 60)
