import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
ps = PorterStemmer()
words = ["connected", "connecting", "connection",
         "playing", "played", "player",
         "studies", "studying", "studied"]

print("Original Word\tStemmed Word")

for word in words:
    stem = ps.stem(word)
    print(f"{word}\t\t{stem}")
