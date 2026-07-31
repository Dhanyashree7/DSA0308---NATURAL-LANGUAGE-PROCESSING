import re
email_pattern= re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|edu|in)$')
emails=["student@gmail.com",
        "abc1232gmail.com",
        "user@college.edu",
        "test@comapny.org",
        "hello123@website.in",
        "wrongemail.com"]
for email in emails:
    if email_pattern.fullmatch(email):
        print(email,"-> valid email ID")
    else:
        print(email,"-> invalid email ID")