corpus = [
    [("The","DT"),("boy","NN"),("eats","VBZ"),("rice","NN")],
    [("The","DT"),("girl","NN"),("drinks","VBZ"),("milk","NN")],
    [("A","DT"),("cat","NN"),("drinks","VBZ"),("milk","NN")],
    [("The","DT"),("dog","NN"),("chases","VBZ"),("cat","NN")],
    [("A","DT"),("teacher","NN"),("teaches","VBZ"),("students","NNS")],
    [("Students","NNS"),("study","VBP"),("English","NN")],
    [("Birds","NNS"),("fly","VBP"),("high","RB")],
    [("Children","NNS"),("play","VBP"),("games","NNS")]
]
emission = {}
transition = {}
tag_count = {}
print("Training Corpus\n")
for sentence in corpus:
    words = []
    tags = []
    for word, tag in sentence:
        words.append(word)
        tags.append(tag)
        tag_count[tag] = tag_count.get(tag,0) + 1
        if tag not in emission:
            emission[tag] = {}
        emission[tag][word] = emission[tag].get(word,0) + 1
    print("Words :", words)
    print("Tags  :", tags)
    print()
    for i in range(len(tags)-1):
        t1 = tags[i]
        t2 = tags[i+1]
        if t1 not in transition:
            transition[t1] = {}
        transition[t1][t2] = transition[t1].get(t2,0) + 1
print("\nEmission Probability\n")
for tag in emission:
    print(tag)
    for word in emission[tag]:
        prob = emission[tag][word] / tag_count[tag]
        print(word,"=",round(prob,3))
    print()
print("\nTransition Probability\n")
for t1 in transition:
    total = sum(transition[t1].values())
    print(t1)
    for t2 in transition[t1]:
        prob = transition[t1][t2] / total
        print(t1,"->",t2,"=",round(prob,3))
    print()
sentence = ["The","cat","drinks","milk"]
print("\nPredicted POS Tags\n")
result = []
for word in sentence:
    best_tag = ""
    best = 0
    for tag in emission:
        if word in emission[tag]:
            prob = emission[tag][word] / tag_count[tag]
            if prob > best:
                best = prob
                best_tag = tag
    if best_tag == "":
        best_tag = "NN"
    result.append(best_tag)
for w,t in zip(sentence,result):
    print(w,"->",t)
print("\nFinal POS Sequence")
print(result)
