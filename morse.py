import tkinter as tk
from tkinter import messagebox

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

class MorseCodeAppGUI:
    def __init__(self, root):
        self.root = root
        self.translator = MorseCodeTranslator(MORSE_CODE_DICT)
        self.root.title("MorseDecoder")
        self.root.iconbitmap("icon/LOGO.ico")

        # Create frames
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Input and output text areas
        self.input_label = tk.Label(self.frame, text="Input text:")
        self.input_label.grid(row=0, column=0, sticky=tk.W)
        self.input_text = tk.Text(self.frame, height=5, width=50)
        self.input_text.grid(row=1, column=0, columnspan=2, pady=5)

        self.output_label = tk.Label(self.frame, text="Output Text:")
        self.output_label.grid(row=2, column=0, sticky=tk.W)
        self.output_text = tk.Text(self.frame, height=5, width=50)
        self.output_text.grid(row=3, column=0, columnspan=2, pady=5)

        # Buttons
        self.encrypt_button = tk.Button(self.frame, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.grid(row=4, column=0, pady=5)

        self.decrypt_button = tk.Button(self.frame, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.grid(row=4, column=1, pady=5)

    def encrypt_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip().upper()
        if input_text:
            encrypted_text = self.translator.encrypt(input_text)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, encrypted_text)
        else:
            messagebox.showerror("Input Error", "Please enter text to encrypt.")

    def decrypt_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        if input_text:
            decrypted_text = self.translator.decrypt(input_text)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, decrypted_text)
        else:
            messagebox.showerror("Input Error", "Please enter Morse code to decrypt.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeAppGUI(root)
    root.mainloop()
