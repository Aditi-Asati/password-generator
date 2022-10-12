import random


def generate_pin(length):
    pin = ""
    for _ in range(length):
        pin += str(random.randint(0, 9))

    return pin


def save_pin(account, pin):
    with open("pins.txt", "a") as f:
        f.write(f"{account}: {pin}\n")


if __name__ == "__main__":
    try:
        account = input("Enter the account name you want to generate a pin for: ")
        length = int(input("How long do you want the pin to be? "))
        pin = generate_pin(length)
        save_pin(account, pin)
        print(f"Here is your pin for {account}: {pin}.")

    except ValueError:
        print("Invalid input!")

    except Exception as e:
        print(f"An unknown error occured: {e}.")
