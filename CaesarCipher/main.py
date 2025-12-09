import string
from art import logo

CHARS = string.printable

def shift_letter(letter, shift) -> str:
    index = CHARS.find(letter)
    if index == -1:
        return letter
    return CHARS[(index + shift) % len(CHARS)]

def perform_caesar_cipher(message, shift):
    return "".join([shift_letter(letter, shift) for letter in message])

def take_user_input():
    print("Type your message:")
    message = input("> ")
    print("Type the shift number:")
    while True:
        raw = input("> ")
        if raw.lstrip("-").isdigit():
            shift = int(raw)
            return message, shift
        print("Please enter an integer for the shift.")


def main() -> None:
    print(logo)
    choice = "yes"
    while True:
        print("Type 'encode' to encrypt, type 'decode' to decrypt")
        user_mode = input("> ").strip().lower()

        if user_mode not in ("encode", "decode"):
            print("Invalid choice. Please type 'encode' or 'decode'.")
            continue

        message, shift = take_user_input()
        if user_mode == "decode":
            shift = -shift

        result = perform_caesar_cipher(message, shift)
        print(f"Result: {result}")

        print("Type 'yes' if you want to go again. Otherwise type 'no'.")
        choice = input("> ").strip().lower()
        if choice != "yes":
            break

if __name__ == "__main__":
    print(len(CHARS))
    print(CHARS)
    main()
