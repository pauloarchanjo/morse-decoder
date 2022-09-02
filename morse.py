MORSE_CODE_DICT = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
}


def encryptor(text):
    encrypted_text = ""
    for letters in text:
        if letters != " ":
            encrypted_text = encrypted_text + MORSE_CODE_DICT.get(letters) + " "
        else:
            encrypted_text += " "
    print("Texto Criptografado: ", encrypted_text)


def decryptor(text):
    text += " "
    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    morse = ""
    normal = ""
    for letters in text:
        if letters != " ":
            morse += letters
            space_found = 0
        else:
            space_found += 1
            if space_found == 2:
                normal += " "
            else:
                normal = normal + key_list[val_list.index(morse)]
                morse = ""
    print("Texto Descriptografado: ", normal)

while True:

    print("====================================================================")
    print("\n\t\t   <<<GERADOR DE CÓDIGO MORSE>>>\n")
    ch = input("\t (E) - Encriptar \t (D) - Descriptografar  \n\n\t\t           (S) - Sair\n")

    if ch == 'E' or ch == 'e':
        text_to_encrypt = input("\nDigite o texto para ser encriptado: ").upper()
        encryptor(text_to_encrypt)
    elif ch == 'D' or ch == 'd':
        text_to_decrypt = input("\nDigite o código morse para descriptografar: ")
        decryptor(text_to_decrypt)
    if ch == 'S' or ch == 's':
        print("\nSaindo do Programa...")
        break
    
