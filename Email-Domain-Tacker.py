# Sample Input
students = [
    {"name": "Rina", "email": "rina@gmail.com"},
    {"name": "Ali", "email": "ali@yahoo.com"},
    {"name": "Zayn", "email": "zayn@gmail.com"},
    {"name": "Lana", "email": "lana@data.com"},
    {"name": "Ali", "email": "ali@yahoo.com"}
]
gmail = []

for student in students:
    email = student["email"]
    if email.endswith("gmail.com"):
        gmail.append(student["name"])
    
    
print(gmail)
