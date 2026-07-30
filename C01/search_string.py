import re

# Given passage
text = """
Artificial Intelligence (AI) is transforming industries across the world. AI is used in healthcare to assist doctors in diagnosis, in
banking to detect fraud, and in education to provide personalized learning experiences. Many companies invest heavily in AI
research because AI improves efficiency and enables intelligent decision-making. As AI continues to evolve, professionals with AI
skills are in high demand.
"""

# Search for the first occurrence of "AI"
match = re.search(r"AI", text)

if match:
    print("1. First occurrence of 'AI' found.")
    print("2. Starting position:", match.start())
    print("3. Ending position:", match.end())

    # Count total occurrences
    count = len(re.findall(r"AI", text))
    print("4. Total number of occurrences:", count)
else:
    print("5. The word 'AI' was not found in the passage.")
