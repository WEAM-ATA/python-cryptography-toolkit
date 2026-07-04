#import modules 
from modules.hash import hash_file , verify_integrity
from modules.encryption import aes_ed ,rsa_ed 
from modules.session_key_destibution import skd
from modules.Message_Authentcaion_code import h_mac
import secrets
#The main menu
def menu():
    print(" Select opertion")
    print("1. Symmetric Encryption (AES)")
    print("2. Asymmetric Encryption (RSA)")
    print("3. Hash file Session Key Distribution")
    print("4. Hash file ")
    print("5. Verify integrity")
    print("6. Message Authentication  Code")
    print("0. Exit")



print(""" Initiate Cryptograpy Toolkit v1.0 ...
      /nWelcome , Agent ! your mission ,should choose to accept it :
      - Analyze and hash files to delete tampering .
      - Encrypt and Decrypt messages with AES and RSA 
      -
      All System online .Date protection is active .
      prepare to enter the world of digital secrecy !! """)
#wile loop to check agent .choise each time 
while True : 
    menu()
    choice = input("Enter choise(0-6)")
    if choice == "0":
        break
    elif choice == "3" :
        file_path = input(" Enter the path of the file ")
        print(" the hashed file is ", hash_file(file_path))
    elif choice == "2":
        f1 = input(" Enter file path 1 ")
        f2 = input(" Enter file path 2 ")
        print(verify_integrity(f1,f2))
    elif choice == "1":
        message = input("Enter a measssage : ")
        key , cipher , plaintext = aes_ed(message)
        print("AES KEY :", key )
        print("AES cipher text :" , cipher )
        print("AES plain text : ", plaintext)
    elif choice == "4":
        message = input("Enter a message : ")
        private_pem , public_pem , ciphertext , plaintext = rsa_ed(message)
        print("the key for encryting is :" , public_pem)
        print("the key for decrypting :", private_pem)
        print("RSA cipher text : ",ciphertext )
        print("RSA plain text :" ,plaintext)
    elif choice == "5":
        key = secrets.token_bytes(32)
        print(skd(key))
    elif choice == "6":
       

       
        key = secrets.token_bytes(32)
        message = input("Enter Message to make HMAC")
        print (h_mac(message , key))

#entering number out of range 
    else:
      print("Invalide choice")

   
print("Agent , You are exiting your cryptography toolkit , stay sharp and secure  ")