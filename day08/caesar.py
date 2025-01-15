from art import logo
import string

class CaeserCipher:
    def __init__(self):
        self.alphabet = string.ascii_lowercase

    def encrypt_decrypt(self, text: str, shift, direction):
        """Encrypts or decrypts the given text based on the direction"""
        shift %= 26
        if direction == "decode":
            shift *= -1

        result = ""
        for char in text:
            if char.isalpha():
                position = self.alphabet.index(char)
                new_position = position + shift
                result += self.alphabet[new_position]
            else:
                result += char
        return result

class CaesarCipherApp:
    def __init__(self):
        self.cipher = CaeserCipher()

    def run(self):
        """Runs the Caeser Cipher application"""
        run = True
        while run:
            print(logo)
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:").strip().lower()
            if direction not in ['encode', 'decode']:
                print("Invalid direction! Please type 'encode' or 'decode'")
                continue

            text = input("Type your message: ").strip().lower()
            try:
                shift = int(input("Type the shift number:").strip())
            except ValueError:
                print("Invalid input! Please enter a number for the shift.")
                continue

            result = self.cipher.encrypt_decrypt(text, shift, direction)
            print(f"Here's the {direction}d result: {result}")

            end = input("Do you want to continue? (y/n): ")
            if end.lower().startswith('n'):
                run = False
                print("Goodbye!")

if __name__ == "__main__":
    app = CaesarCipherApp()
    app.run()
