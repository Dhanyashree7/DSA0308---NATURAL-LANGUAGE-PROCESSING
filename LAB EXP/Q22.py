sentence = input("Enter sentence: ")

words = sentence.split()

previous_noun = ""

for word in words:

    if word.lower() in ["he", "she", "it", "they"]:
        print(word, "refers to", previous_noun)

    elif word[0].isupper() or word.lower() in ["boy", "girl", "dog", "cat"]:
        previous_noun = word
