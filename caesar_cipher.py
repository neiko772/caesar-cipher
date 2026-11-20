# caesar_cipher.py
# Encodes and decodes robotics club scavenger hunt clues with a Caesar cipher.

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plain_text, shift):
    cipher_text = ""
    for letter in plain_text:
        position = ALPHABET.index(letter)
        new_position = (position + shift) % 26
        cipher_text += ALPHABET[new_position]
    return cipher_text




def decrypt(cipher_text, shift):
    plain_text = ""
    for letter in cipher_text:
        position = ALPHABET.index(letter)
        new_position = (position - shift) % 26
        plain_text += ALPHABET[new_position]
    return plain_text


def caesar(text, shift, direction):
    if direction == "decode":
        shift = shift * -1
    result = ""
    for letter in text:
        if letter in ALPHABET:
            position = ALPHABET.index(letter)
            new_position = (position + shift) % 26
            result += ALPHABET[new_position]
        else:
            result += letter
    return result




def ask_direction():
    """Ask until the user types encode or decode, then return it."""
    direction = input("Type encode or decode:").strip().lower()
    while direction != "encode" and direction != "decode":
        print("Type encode or decode, spelled exactly")
        direction = input("Type encode or decode:").strip().lower()
    return direction


def ask_shift():
    """Ask until the user types a whole number, then return it as an int."""
    while True:
        answer = input("Shift number:")
        try:
            return int(answer)
        except ValueError:
            print("Type a whole number, like 3")


def main():
    print("Robotics Club Clue Machine")

    again = "yes"
    while again == "yes":
        direction = ask_direction()
        message = input("Enter your message:").lower()
        shift = ask_shift()

        result = caesar(text=message, shift=shift, direction=direction)
        print("Result:", result)

        again = input("Type yes to go again:").strip().lower()
        print("Club machine off.")

main() 