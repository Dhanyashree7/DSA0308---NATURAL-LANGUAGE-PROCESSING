import math

documents = [
    "natural language processing",
    "machine learning",
    "natural language learning"
]

query = input("Enter query: ").lower().split()

for i, document in enumerate(documents):

    words = document.split()
    score = 0

    for word in query:

        tf = words.count(word) / len(words)

        df = 0
        for doc in documents:
            if word in doc.split():
                df += 1

        if df > 0:
            idf = math.log(len(documents) / df)
            score = score + tf * idf

    print("Document", i + 1, "Score:", round(score, 3))
