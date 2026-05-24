import re
password = input("Enter your password:")
strength = 0
#الطول
if len(password) >= 8:
    strength += 1

#حروف كبيرة وصغيرة
if re.search(r"[A-Z]", password) and re.search(r"[A-Z`]", password):
    strength += 1

#أرقام
if re.search(r"\d", password):
    strength += 1

#رموز
if re.search(r"[!@#$%^&*]", password):
    strength += 1

#النتيجة
print("Password Score:", strength, "/4")
if strength == 4:
    print("Strong Password")
elif strength == 3:
    print("Medium Password")
else:
    print("Weak Password")