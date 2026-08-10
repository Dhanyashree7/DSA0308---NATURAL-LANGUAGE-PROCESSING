sentence = input("Enter sentence: ").lower().split()
singular = ["boy", "girl", "cat"]
plural = ["boys", "girls", "cats"]
if len(sentence) == 2:
    subject = sentence[0]
    verb = sentence[1]
    if subject in singular and verb.endswith("s"):
        print("Agreement Correct")
    elif subject in plural and not verb.endswith("s"):
        print("Agreement Correct")
    else:
        print("Agreement Incorrect")
else:
    print("Invalid sentence")
