import re

# Sample text
text = "My email is student123@gmail.com and my phone number is 9876543210."

# 1. Match: Checks only at the beginning of the string
match_result = re.match(r"My", text)

if match_result:
    print("Match found:", match_result.group())
else:
    print("No match found")

# 2. Search: Finds the first occurrence anywhere in the string
search_result = re.search(r"email", text)

if search_result:
    print("Search found:", search_result.group())
else:
    print("Search not found")

# 3. Find an email address
email = re.search(r"\S+@\S+\.\S+", text)

if email:
    print("Email:", email.group())

# 4. Find a 10-digit phone number
phone = re.search(r"\d{10}", text)

if phone:
    print("Phone Number:", phone.group())
