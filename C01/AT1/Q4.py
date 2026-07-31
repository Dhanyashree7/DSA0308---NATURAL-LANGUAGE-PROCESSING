import re 
email=input("Enter Email ID:")
password= input("Enter Strong Password:")

email_pattern= r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|edu|in)$'

password_pattern= r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!*])[A-Za-z\d@#$%&!*]{8,}$'
if re.fullmatch(email_pattern,email):
    print("valid email ID")
else:
    print("invalid email ID")
if re.fullmatch(password_pattern,password):
    print("strong password")
else:
    print("invalid password")