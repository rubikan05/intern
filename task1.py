def encryption(plain_text, shift_key):
    
    cipher_text = ""
    for char in plain_text:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            position = 'abcdefghijklmnopqrstuvwxyz'.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += 'abcdefghijklmnopqrstuvwxyz'[new_position]
        else:
            cipher_text += char
    return cipher_text

def decryption(cipher_text, shift_key):
    
    plain_text = ""
    for char in cipher_text:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            position = 'abcdefghijklmnopqrstuvwxyz'.index(char)
            new_position = (position - shift_key) % 26
            plain_text += 'abcdefghijklmnopqrstuvwxyz'[new_position]
        else:
            plain_text += char
    return plain_text

plain_text = input("enter the text")
shift_key = int (input("enter shift value"))
cipher_text = encryption(plain_text, shift_key)
print("Plain text:", plain_text)
print("Shift key:", shift_key)
print("Cipher text:", cipher_text)

decrypted_text = decryption(cipher_text, shift_key)
print("Decrypted text:", decrypted_text)
