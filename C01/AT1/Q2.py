import re
text="""
artificial intellegent(AI) is transforming industries across the world AI is used in healthcare to assist doctors in diagnosis, in banking to detect fraud. and in education to provide personalized learning experience. many companies invest heavily in AI research because AI improves efficiency and enable intellegent decision_making. As AI continues to evolve, professional with AI skills are in high demand
"""
match=re.search(r"AI",text)
if match:
    print("1. First occurence of 'AI' found.")
    print("2. Starting position:",match.start())
    print("3. Ending position:",match.end())
    count=len(re.findall(r"AI",text))
    print("4. Total number of occurence:",count)
else:
    print("5. The word 'AI' was not found in the passage.")