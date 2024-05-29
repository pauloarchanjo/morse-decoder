MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

class MorseCodeTranslator:
    def __init__(self, code_dict):
        self.code_dict = code_dict
        self.inverse_code_dict = {v: k for k, v in code_dict.items()}
    
    def encrypt(self, text):
        encrypted_text = []
        for letter in text:
            if letter != " ":
                encrypted_text.append(self.code_dict.get(letter, ""))
            else:
                encrypted_text.append(" ")
        return " ".join(encrypted_text)
    
    def decrypt(self, morse_text):
        morse_text += " "
        morse_characters = []
        normal_text = []
        for char in morse_text:
            if char != " ":
                morse_characters.append(char)
                space_found = 0
            else:
                space_found += 1
                if space_found == 2:
                    normal_text.append(" ")
                else:
                    morse_letter = "".join(morse_characters)
                    normal_text.append(self.inverse_code_dict.get(morse_letter, ""))
                    morse_characters = []
        return "".join(normal_text)

class MorseCodeApp:
    def __init__(self):
        self.translator = MorseCodeTranslator(MORSE_CODE_DICT)
    
    def run(self):
        while True:
            print("====================================================================")
            print("\n\t\t   <<< MORSE CODE ENCRYPTOR >>>\n")
            print("====================================================================")
            print("Choose your option: \n")
            choice = input("(E) - Encrypt \n\n(D) - Decrypt  \n\n(S) - Exit Program\n").upper()
            if choice == 'E':
                text_to_encrypt = input("\nEnter text to be encrypted: ").upper()
                encrypted_text = self.translator.encrypt(text_to_encrypt)
                print("Encrypted text: ", encrypted_text)
            elif choice == 'D':
                text_to_decrypt = input("\nEnter text to be decrypted: ")
                decrypted_text = self.translator.decrypt(text_to_decrypt)
                print("Decrypted text: ", decrypted_text)
            elif choice == 'S':
                print("\n Shutdown...")
                break
            else:
                print("\nInvalid option. Try again.")

if __name__ == "__main__":
    app = MorseCodeApp()
    app.run()
