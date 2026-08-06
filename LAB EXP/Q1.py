import re
text = "My email is student123@gmail.com and my phone number is 9876543210."
email = re.search(r"\S+@\S+", text)
phone = re.search(r"\d{10}", text)
print("Original Text:")
print(text)
if email:
    print("\nEmail Found:", email.group())
if phone:
    print("Phone Number Found:", phone.group())
