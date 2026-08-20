from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import re
import time

stemmer = PorterStemmer()

documents = [
    "connected connection connecting connectivity",
    "studies studied studying study",
    "organize organized organizer organization",
    "students study computer science",
    "researchers are studying machine learning",
    "organizations organized educational programs"
]


# ---------------- ORIGINAL PIPELINE ----------------

start = time.time()

vectorizer_original = CountVectorizer()

X_original = vectorizer_original.fit_transform(documents)

original_vocabulary = vectorizer_original.get_feature_names_out()

original_time = time.time() - start


# ---------------- CORRECTED PIPELINE ----------------

def normalize(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return " ".join(stemmer.stem(word) for word in words)


start = time.time()

normalized_documents = [
    normalize(doc)
    for doc in documents
]

vectorizer_corrected = CountVectorizer()

X_corrected = vectorizer_corrected.fit_transform(
    normalized_documents
)

corrected_vocabulary = vectorizer_corrected.get_feature_names_out()

corrected_time = time.time() - start


# ---------------- OUTPUT ----------------

print("MORPHOLOGICAL PREPROCESSING ERROR ANALYSIS")
print("=" * 65)

print("\nORIGINAL VOCABULARY")
print("-" * 65)

print(list(original_vocabulary))

print("\nOriginal Vocabulary Size:",
      len(original_vocabulary))


print("\nNORMALIZED DOCUMENTS")
print("-" * 65)

for doc in normalized_documents:
    print(doc)


print("\nCORRECTED VOCABULARY")
print("-" * 65)

print(list(corrected_vocabulary))

print("\nCorrected Vocabulary Size:",
      len(corrected_vocabulary))


print("\nVOCABULARY COMPARISON")
print("-" * 65)

print("Before Correction:",
      len(original_vocabulary))

print("After Correction :",
      len(corrected_vocabulary))

print("Reduction        :",
      len(original_vocabulary) - len(corrected_vocabulary))


print("\nPROCESSING TIME")
print("-" * 65)

print("Original Pipeline :",
      round(original_time, 6), "seconds")

print("Corrected Pipeline:",
      round(corrected_time, 6), "seconds")
