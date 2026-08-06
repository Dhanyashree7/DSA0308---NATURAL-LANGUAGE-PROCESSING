import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The cat drinks milk"

words = nltk.word_tokenize(text)

tags = nltk.pos_tag(words)

print("Words with POS Tags:")

for word, tag in tags:
    print(word, "->", tag)
