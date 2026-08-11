grammar = {
    "S": ["NP VP"],
    "NP": ["Det N"],
    "VP": ["V"],
    "Det": ["the"],
    "N_Singular": ["boy", "girl", "student"],
    "N_Plural": ["boys", "girls", "students"],
    "V_Singular": ["runs", "plays", "eats"],
    "V_Plural": ["run", "play", "eat"]
}
def check_agreement(sentence):
    words = sentence.lower().split()
    if len(words) != 3:
        return "Sentence should have exactly 3 words"
    determiner, noun, verb = words
    if determiner != "the":
        return "Sentence is not agreement"
    if noun in grammar["N_Singular"] and verb in grammar["V_Singular"]:
        return "Sentence is agreement"
    elif noun in grammar["N_Plural"] and verb in grammar["V_Plural"]:
        return "Sentence is agreement"
    else:
        return "Sentence is not agreement"
sentences = {
    "the boy runs",
    "the girl plays",
    "the boys eat",
    "the girls eat",
    "the boy run",
    "the boys runs"
}
for sentence in sentences:
    print(f"{sentence} -> {check_agreement(sentence)}")
