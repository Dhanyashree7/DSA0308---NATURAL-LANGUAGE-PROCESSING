grammar={
"S":["NP VP"],
"NP":["Det N"],
"VP":["V"],
"Det":["the"],
"N_singular":["boy","girl","student"],
"N_plural":["boys","girls","students"],
"V_singular":["runs","plays","eats"],
"V_plural":["run","play","eat"]
}
def check agreement(sentence):
words=sentence.lower().spli()
if len(words)!=3:
print("Sentence should have 3 words:")
det,noun,verb=words
if det!="the":
print("sentence noi in agreement:")
if noun in grammar["N_Singular"] and verb in grammar["V_Singular"]:
print("Sentence in agreement:")
elif noun in grammer["N_plural"] and verb in grammar["V_plural"]:
print("Sentence in agreement:")
else:
print("not in agreement:")
sentences={
"the boy runs",
"the girl plays",
"the boys eat",
"the girls eat",
"the boy run",
"the boys runs"
}
for sentence in sentences:
print(f"{sentence} -{check_agreement(sentence)}")







































