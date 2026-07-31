import re
text="""
Artificial intellegent (AI) is transformed industries across the world. AI is used in healthcare to assist doctors in diagnosis, in banking to detect fraud, and in education to provide personalized learning experience. many companies invest heavily in AI research because AI improve efficeiency and enable intellegent decision_making. As AI continue to evolve, professionals with AI skills are in high demand."
"""
sentences= re.split(r'[.!?]+',text)
sentences=[s.strip() for s in sentences if s.strip()]
print("Total number of sentences:",len(sentences))
print("\nList of sentences:")
for i, sentence in enumerate(sentences,1):
    print(f"{i}.{sentence}")
words= re.split(r'\s+',text.strip())
print("\nTotal number of words:",len(words))
print("\nList of Words:")
print(words)