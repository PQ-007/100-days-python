import caesar_art

print(caesar_art.ascii)

def decode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            result += shifted_char
        else:
            result += char
    return result

def encode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            result += shifted_char
        else:
            result += char
    return result

running = True
while running:
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    direction = input("Type here: ")
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    if direction == "encode":
        print(f"Encoded text: {encode(text, shift)}")
    elif direction == "decode":
        print(f"Decoded text: {decode(text, shift)}")
    else:
        print("Invalid direction. Please choose 'encode' or 'decode'.")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if restart.lower() != "yes":
        running = False
        print("Goodbye!")