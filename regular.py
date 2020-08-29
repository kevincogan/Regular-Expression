import re
import csv

data_base = ["kevincogan", 'kcogan']
regex = '^[a-z0-9]+[\._]?[a-z0-9]*[\._]?[a-z0-9]*[@]\w+[.]?\w+?[.]\w{2,3}$'

def hasNumbers(password):
    return bool(re.search(r'\d', password))

def check(email):
    if(re.search(regex,email)):
        print("Valid Email")
        return "good"

    else:
        print("Invalid Email")

#Username
status = "bad"
while status == "bad":
    username = str(input("Enter username: "))
    if len(username) >= 8 and username not in data_base:
        status = "good"

    #Warning notices
    if username in data_base:
        print("Username taken please select another")
    else:
        data_base.append(username)
        print(data_base)

    if len(username) < 8:
        print("Username needs to be 8 or greater than 8 character")

#Password
status = "bad"
while status == "bad":
    password = str(input("Enter password: "))
    if len(username) >= 8 and hasNumbers(password):
        status = "good"

#Email
status = "bad"
while status == "bad":
    email = input("Enter email address: ")
    status = check(email)

if status == "good":
    print()
    print("Thank you! You are ready to go!")

user = {username:[password, email]}
print(user)

#CSV Writer
with open('users.csv', 'a+', newline='') as file:
    fieldnames = ['user_name', 'password', 'email']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    #writer.writeheader()
    writer.writerow({'user_name': username, 'password': password, 'email': email})
