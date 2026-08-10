grammar = {
    "Det": {"the": 1.0, "a": 1.0},
    "N": {"boy": 0.6, "girl": 0.4},
    "V": {"eats": 0.7, "likes": 0.3}
}
sentence = input("Enter sentence: ").lower().split()
probability = 1
if sentence[0] in grammar["Det"]:
    probability *= grammar["Det"][sentence[0]]
else:
    probability = 0
if sentence[1] in grammar["N"]:
    probability *= grammar["N"][sentence[1]]
else:
    probability = 0
if sentence[2] in grammar["V"]:
    probability *= grammar["V"][sentence[2]]
else:
    probability = 0
print("Probability:", probability)
if probability > 0:
    print("Sentence Accepted")
else:
    print("Sentence Rejected")
