# def encrypt(text, shift):
#     encrypted_text = ""

#     for letter in text:
#         index = alphabet.index(letter)
#         new_index = (index + shift) % 26
#         encrypted_text += alphabet[new_index]
#     print("The encoded text is " + encrypted_text)


# def decrypt(text, shift):
#     decrypted_text = ""

#     for letter in text:
#         index = alphabet.index(letter)
#         new_index = (index - shift) % 26
#         decrypted_text += alphabet[new_index]
#     print("The decrypted text is " + decrypted_text)

import art

def caesar_cipher(input_text, shift, direction):
    output_text = ""
    for letter in input_text:
        if letter.isalpha():
            index = alphabet.index(letter)
            if direction == "encode":
                new_index = (index + shift) % 26
            else:
                new_index = (index - shift) % 26
            output_text += alphabet[new_index]
        else:
            output_text += letter
    print(f"The {direction}d text is {output_text}")

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(input_text=text, shift=shift, direction=direction)

    cont = input("Enter 'yes' if you wanna go again. Otherwise type 'no'\n")
    if cont == "no":
        break