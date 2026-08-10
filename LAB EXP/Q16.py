import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple is located in California. Tim Cook is the CEO."
doc = nlp(text)
print("Named Entities:")
for entity in doc.ents:
    print(entity.text, "->", entity.label_)
