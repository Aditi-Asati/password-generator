# Password generator
import string as stg
import random, datetime


class PasswordConfig:
    def __init__(self):
        self.password_length = 16

        # list of all lowercase alphabets
        self.lower_case = list(stg.ascii_lowercase)

        # list of all uppercase alphabets
        self.upper_case = list(stg.ascii_uppercase)

        # list of all digits
        self.digits = list(stg.digits)

        # list of all special characters
        self.punctuation = list(stg.punctuation)

        # Characters not allowed in a password according to IBM
        pop_items = ['"', "'", ",", "/", "<", ">", "\\", "{", "}", "|"]

        for item in pop_items:
            self.punctuation.remove(item)

    def get_char_ranges(self) -> list[list[str]]:
        return [self.lower_case, self.upper_case, self.digits, self.punctuation]

    def set_length(self, password_length: int):
        self.password_length = password_length


def main():
    conf = PasswordConfig()

    account = input("Enter the account for which you want to generate the password: ")

    n = int(
        input(
            "Enter the number of characters you want your password to consist of "
            "(Please remember that your password must contain minimum 5 characters): "
        )
    )

    conf.set_length(n)

    password = generate_password(conf)

    print(password)

    # Storing the created password in a txt file
    with open("passwords.txt", "a") as f:
        f.write(password + f" - generated at {datetime.datetime.now()} for {account}\n")


def generate_password(conf: PasswordConfig) -> str:
    # initializing the password
    password = ""
    validated = False
    while not validated:
        # to ensure that the password has minimum 1 lowercase, uppercase, digit, and character
        char_ranges = conf.get_char_ranges()

        ranges_count = 4
        for _ in range(ranges_count):
            char_range = random.choice(char_ranges)
            char = random.choice(char_range)
            password = password + char
            char_ranges.remove(char_range)

        # randomly filling up the remaining password characters
        char_ranges = conf.get_char_ranges()

        for _ in range(conf.password_length - ranges_count):
            char_range = random.choice(char_ranges)
            char = random.choice(char_range)
            password = password + char

        if password[0] == ".":
            validated = False
        elif password[0] == "-":
            validated = False
        else:
            validated = True
    # shuffling characters of the password random no of times
    for _ in range(random.randint(3, 10)):
        password = "".join(random.sample(password, len(password)))
    return password


if __name__ == "__main__":
    main()
