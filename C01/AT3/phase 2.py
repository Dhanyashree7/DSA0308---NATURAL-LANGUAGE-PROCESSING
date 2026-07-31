# -------------------------------
# PORTER STEMMER - PART 1
# Basic Utility Functions
# -------------------------------

class PorterStemmer:

    def __init__(self):
        pass

    # Check whether a character is a consonant
    def is_consonant(self, word, i):
        ch = word[i]

        if ch in "aeiou":
            return False

        if ch == "y":
            if i == 0:
                return True
            return not self.is_consonant(word, i - 1)

        return True

    # Calculate measure (m)
    def measure(self, stem):
        m = 0
        i = 0
        length = len(stem)

        while i < length:
            while i < length and self.is_consonant(stem, i):
                i += 1

            while i < length and not self.is_consonant(stem, i):
                i += 1
                if i <= length:
                    m += 1

        return m

    # Check whether stem contains a vowel
    def contains_vowel(self, stem):
        for i in range(len(stem)):
            if not self.is_consonant(stem, i):
                return True
        return False

    # Check double consonant
    def double_consonant(self, word):
        if len(word) < 2:
            return False

        if word[-1] != word[-2]:
            return False

        return self.is_consonant(word, len(word) - 1)

    # Check cvc ending
    def cvc(self, word):

        if len(word) < 3:
            return False

        if (not self.is_consonant(word, -1) or
            self.is_consonant(word, -2) or
            not self.is_consonant(word, -3)):
            return False

        if word[-1] in "wxy":
            return False

        return True
# -------------------------------
# PORTER STEMMER - PART 2
# Step 1a, Step 1b, Step 1c
# -------------------------------

    # Step 1a
    def step1a(self, word):

        if word.endswith("sses"):
            return word[:-2]

        elif word.endswith("ies"):
            return word[:-2]

        elif word.endswith("ss"):
            return word

        elif word.endswith("s"):
            return word[:-1]

        return word


    # Step 1b
    def step1b(self, word):

        if word.endswith("eed"):
            stem = word[:-3]
            if self.measure(stem) > 0:
                return stem + "ee"

        elif word.endswith("ed"):
            stem = word[:-2]

            if self.contains_vowel(stem):
                word = stem

                if word.endswith("at"):
                    word += "e"

                elif word.endswith("bl"):
                    word += "e"

                elif word.endswith("iz"):
                    word += "e"

                elif self.double_consonant(word) and word[-1] not in "lsz":
                    word = word[:-1]

                elif self.measure(word) == 1 and self.cvc(word):
                    word += "e"

                return word

        elif word.endswith("ing"):
            stem = word[:-3]

            if self.contains_vowel(stem):
                word = stem

                if word.endswith("at"):
                    word += "e"

                elif word.endswith("bl"):
                    word += "e"

                elif word.endswith("iz"):
                    word += "e"

                elif self.double_consonant(word) and word[-1] not in "lsz":
                    word = word[:-1]

                elif self.measure(word) == 1 and self.cvc(word):
                    word += "e"

                return word

        return word


    # Step 1c
    def step1c(self, word):

        if word.endswith("y"):

            stem = word[:-1]

            if self.contains_vowel(stem):
                return stem + "i"

        return word
# -------------------------------
# PORTER STEMMER - PART 3
# Step 2 and Step 3
# -------------------------------

    # Step 2
    def step2(self, word):

        suffixes = {
            "ational": "ate",
            "tional": "tion",
            "enci": "ence",
            "anci": "ance",
            "izer": "ize",
            "abli": "able",
            "alli": "al",
            "entli": "ent",
            "eli": "e",
            "ousli": "ous",
            "ization": "ize",
            "ation": "ate",
            "ator": "ate",
            "alism": "al",
            "iveness": "ive",
            "fulness": "ful",
            "ousness": "ous",
            "aliti": "al",
            "iviti": "ive",
            "biliti": "ble"
        }

        for suffix in sorted(suffixes.keys(), key=len, reverse=True):
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.measure(stem) > 0:
                    return stem + suffixes[suffix]

        return word


    # Step 3
    def step3(self, word):

        suffixes = {
            "icate": "ic",
            "ative": "",
            "alize": "al",
            "iciti": "ic",
            "ical": "ic",
            "ful": "",
            "ness": ""
        }

        for suffix in sorted(suffixes.keys(), key=len, reverse=True):
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.measure(stem) > 0:
                    return stem + suffixes[suffix]

        return word
# -------------------------------
# PORTER STEMMER - PART 4
# Step 4, Step 5a, Step 5b
# -------------------------------

    # Step 4
    def step4(self, word):

        suffixes = [
            "al", "ance", "ence", "er", "ic", "able", "ible",
            "ant", "ement", "ment", "ent", "ion",
            "ou", "ism", "ate", "iti", "ous", "ive", "ize"
        ]

        for suffix in sorted(suffixes, key=len, reverse=True):
            if word.endswith(suffix):

                stem = word[:-len(suffix)]

                if suffix == "ion":
                    if len(stem) == 0:
                        continue
                    if stem[-1] not in "st":
                        continue

                if self.measure(stem) > 1:
                    return stem

        return word


    # Step 5a
    def step5a(self, word):

        if word.endswith("e"):

            stem = word[:-1]

            if self.measure(stem) > 1:
                return stem

            if self.measure(stem) == 1 and not self.cvc(stem):
                return stem

        return word


    # Step 5b
    def step5b(self, word):

        if self.measure(word) > 1 and self.double_consonant(word) and word.endswith("l"):
            return word[:-1]

        return word


    # Complete Porter Stemmer
    def stem(self, word):

        word = word.lower()

        word = self.step1a(word)
        word = self.step1b(word)
        word = self.step1c(word)
        word = self.step2(word)
        word = self.step3(word)
        word = self.step4(word)
        word = self.step5a(word)
        word = self.step5b(word)

        return word


# -------------------------------
# Main Program
# -------------------------------

ps = PorterStemmer()

test_words = [
    "caresses","ponies","ties","cats","feed",
    "agreed","plastered","bled","motoring","sing",
    "happy","sky","relational","conditional","rational",
    "valenci","hesitanci","digitizer","conformabli",
    "radicalli","differentli","vileli","analogousli",
    "vietnamization","predication","operator","feudalism",
    "decisiveness","hopefulness","callousness",
    "formaliti","sensitiviti","sensibiliti",
    "triplicate","formative","formalize",
    "electricity","electrical","hopeful","kindness",
    "revival","allowance","inference","airliner",
    "gyroscopic","adjustable","defensible","irritant",
    "replacement","dependent"
]

print("{:<20}{}".format("Original Word", "Stem"))
print("-" * 35)

for word in test_words:
    print("{:<20}{}".format(word, ps.stem(word)))


