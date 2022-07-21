# Password generator
import string as stg
import random, datetime

#list of all lowercase alphabets
lower_case = list(stg.ascii_lowercase)

#list of all uppercase alphabets
upper_case = list(stg.ascii_uppercase)

#list of all digits
digit_s = list(stg.digits)

#list of all special characters
char = list(stg.punctuation)

#Characters not allowed in a password according to IBM
pop_items = ["\"", "'", ",", "/", "<", ">", "\\", "{", "}", "|"]

for item in pop_items:
    char.remove(item)

l = [lower_case, upper_case, digit_s, char]

#initializing the password
password = ""

n = int(input("Enter the number of characters you want your password to consist of (Please remember that your password must contain minimum 5 characters): "))

validated = False
while not validated:
    #to ensure that the password has minimum 1 lowercase, uppercase, digit, and character
    for _ in range(4):
        choose = random.choice(l)
        chr = random.choice(choose)
        password = password+chr
        l.remove(choose)

    #randomly filling up the remaining password characters
    l = [lower_case, upper_case, digit_s, char]

    for _ in range(n-4):
        type = random.choice(l)
        entry = random.choice(type)
        password = password+entry

    if password[0] == ".":
        validated = False
    elif password[0] == "-":
        validated = False
    else:
        validated = True

#shuffling characters of the password random no of times
for _ in range(random.randint(3, 10)):
    password = "".join(random.sample(password, len(password)))

print(password)

#Storing the created password in a txt file
with open("passwords.txt", "a") as f:
    f.write(password+f" - generated at {datetime.datetime.now()}\n")


