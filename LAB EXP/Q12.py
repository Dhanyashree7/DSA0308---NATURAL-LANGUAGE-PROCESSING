grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["boy"], ["girl"], ["apple"]],
    "V": [["eats"], ["likes"]]
}
sentence = input("Enter sentence: ").lower().split()
def parse(symbol, words, pos):
    if symbol not in grammar:
        return pos + 1 if pos < len(words) and words[pos] == symbol else -1
    for rule in grammar[symbol]:
        p = pos
        success = True
        for item in rule:
            p = parse(item, words, p)
            if p == -1:
                success = False
                break
        if success:
            return p
    return -1
result = parse("S", sentence, 0)
if result == len(sentence):
    print("Sentence Accepted")
else:
    print("Sentence Rejected")
