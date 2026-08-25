text = input("Enter dialog: ").lower()

if "?" in text:
    print("Dialog Act: Question")

elif text.startswith("please"):
    print("Dialog Act: Request")

elif text.startswith("yes") or text.startswith("okay"):
    print("Dialog Act: Agreement")

elif "thank" in text:
    print("Dialog Act: Thanking")

elif text.startswith("hello") or text.startswith("hi"):
    print("Dialog Act: Greeting")

else:
    print("Dialog Act: Statement")
