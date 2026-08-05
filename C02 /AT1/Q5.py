from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["relational","relation","relate"]
print("Word\t\tStem")
for word in words:
    print(word,"\t",ps.stem(word))
