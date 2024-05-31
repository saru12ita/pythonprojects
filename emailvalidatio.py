email = input("Please Enter Your Email:")  # g@g.in, bksarita729@gmail.com

def validate_email(email):
    if len(email) < 6:
        return "Wrong Email 1"
    
    if not email[0].isalpha():
        return "Wrong Email 2"
    
    if "@" not in email or email.count("@") != 1:
        return "Wrong Email 3"
    
    if not (email.endswith(".com") or email.endswith(".in")):
        return "Wrong Email 4"

    for i in email:
        if i.isspace():
            return "Wrong Email 5"
        elif i.isalpha():
            if i.isupper():
                return "Wrong Email 5"
        elif i.isdigit():
            continue
        elif i in "_@.":
            continue
        else:
            return "Wrong Email 5"
    
    return "Email is valid"

result = validate_email(email)
print(result)
