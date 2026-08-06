import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
ps = PorterStemmer()
words = ["connected", "connecting", "connection",
         "playing", "played", "player"]

print("Word\t\tStem")

for word in words:
    stem = ps.stem(word)
    print(f"{word}\t\t{stem}")
