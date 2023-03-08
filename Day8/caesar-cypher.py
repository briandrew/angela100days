
from alphanumeric import lower_letters

# def encrypt(plain_text, shift_amount):
#     cipher_text = ''
#     for letter in plain_text:
#         position = lower_letters.index(letter)
#         new_position = position + shift_amount
#         new_letter = lower_letters[new_position]
#         cipher_text += new_letter
#     print(f"The encrypted text is: {cipher_text} ")

# def decrypt(encrypted_text, shift_amount):
#     plain_text = ''
#     for letter in encrypted_text:
#         position = lower_letters.index(letter)
#         new_position = position - shift_amount
#         new_letter = lower_letters[new_position]
#         plain_text += new_letter
#     print(f"The decrypted text is: {plain_text}")

# consolidated single function
def caesar(encrypt_decrypt, text_in, shift_amount):
    text_out = ''
    if encrypt_decrypt == 'decrypt':
        shift_amount *= -1
    for char in text_in:
        if char in lower_letters:
            position = lower_letters.index(char)
            new_position = position + shift_amount
            text_out += lower_letters[new_position]
        else:
            text_out += char
    print(f" The {encrypt_decrypt}ed text is: {text_out}")
    
should_continue = True
while should_continue:
    direction = input("Type 'encrypt' or 'decrypt': ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # in case user enters shift > 26
    caesar(encrypt_decrypt=direction, text_in=text, shift_amount=shift)
    go_again = input("Go again? enter 'yes' or 'no': ")
    if go_again == 'no':
        should_continue = False
        print("Goodbye!")




