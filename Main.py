from os import system
import platform

global alphabet
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def clear_display():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

def generate_key_square(key):
    key = key.replace(" ", "").upper()
    key_square = []
    
    for char in key:
        if char not in key_square:
            key_square.append(char)
    
    for char in alphabet:
        if char not in key_square:
            key_square.append(char)
    
    key_matrix = [key_square[i:i+5] for i in range(0, 25, 5)]
    return key_matrix

def get_position(matrix, char):
    for row in range(len(matrix)):
        if char in matrix[row]:
            col = matrix[row].index(char)
            return row, col
        
        
# Encoding
def encode(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key_matrix = generate_key_square(key)
    
    # Adding 'X' between repeating characters and 'X' for odd-length plaintext
    i = 0
    while i < len(plaintext)-1:
        if plaintext[i] == plaintext[i+1]:
            plaintext = plaintext[:i+1] + 'X' + plaintext[i+1:]
        i += 1
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i+1]
        row1, col1 = get_position(key_matrix, char1)
        row2, col2 = get_position(key_matrix, char2)
        
        if row1 == row2:
            ciphertext += key_matrix[row1][(col1+1)%5] + key_matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += key_matrix[(row1+1)%5][col1] + key_matrix[(row2+1)%5][col2]
        else:
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]
    
    return ciphertext



# Decoding
def decode(ciphertext, key):
    key_matrix = generate_key_square(key)
    ciphertext = ciphertext.replace(" ", "").upper()
    
    plaintext = ""
    for i in range(0, len(ciphertext)-1, 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = get_position(key_matrix, char1)
        row2, col2 = get_position(key_matrix, char2)
        
        if row1 == row2:
            plaintext += key_matrix[row1][(col1-1)%5] + key_matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plaintext += key_matrix[(row1-1)%5][col1] + key_matrix[(row2-1)%5][col2]
        else:
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]
    
    if plaintext[-1] == 'X':
        plaintext = plaintext[:-1]
    
    i = 0
    while i < len(plaintext)-2:
        if plaintext[i] == plaintext[i+2]:
            plaintext = plaintext[:i+1] + plaintext[i+2:]
        i += 1
    
    
    return plaintext

while True:
    clear_display()
    choice = input("Type 'encode' to encrypt\nType 'decode' to decrypt\n==> ")
    if choice == "encode" or choice == "decode":
        text = input("Type your messege : ")
        key = input("Type the key (String) : ")
        
        if choice == "encode":
            print(encode(text, key))
        else:
            print(decode(text, key))
            
        # if choice == "encode":
        #     print(encode("SOFTWARE ENGINEERING", "ASHIK"))
        # else:
        #     print(decode("KLEUVSTDYDOLETDYDTETMV", "Ashik"))
        
    else:
        print("\nWrong Selection\nYou need to type 'encode' to encrypt or 'decode' to decrypt\n")

    isContinue = input("Do you want to continue? (Y/N) : ")
    clear_display()
    if isContinue == 'n' or isContinue == 'N': break
    
print("\n\n---------------------------------------------------")
print("\nGoodbye\nThanks for using....")
print("---------------------------------------------------")
