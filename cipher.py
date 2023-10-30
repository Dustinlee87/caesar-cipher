def encrypt(plain_text, shift):
    plain_text = plain_text.lower()
    encrypted_text = ""
    for i in plain_text:
        if i.islower():
            encrypted_text += chr((ord(i) + shift - 97) % 26 + 97)
        else:
            encrypted_text += i
    return encrypted_text

message = "Hello, my name is Dustin"
encrypted_message = encrypt(message, 5)
print(encrypted_message)# add your code here
