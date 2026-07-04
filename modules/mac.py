#other hash function applications 
import hashlib
import hmac 
import secrets 
from cryptography.hazmat.primitives.asymmetric import rsa , padding
from cryptography.hazmat.primitives import  hashes
import os 
from getpass import getpass
#_________________________________________________________
#..............1. message authentication .................
def mac_gen(massage , key ):
    h = hmac.new(key, massage.encode(),hashlib.sha256)  
    return h.hexdigest()

def verify_mac (recived_massage , recived_mac , key):
    calculated_mac  = mac_gen(recived_massage,key)
    if hmac.compare_digest(calculated_mac,recived_mac):
        print ("Verfication successful :Massage is authentic ")
    print("Verification failed : Massage or MAC has been modified ")




#_________________________________________________________
# ...............2. digital signature..................... 
#sender side 
def digiral_signature_genrateenhased(message, private_key):
    #encrypt the hashed value using user private key 
    signature = private_key.sign(
        message.encode(),
        padding.PSS (
            mgf = padding.MGF1(hashes.SHA256()),
            salt_length= padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature 
# reciver side 
def verify_signature( message ,signature,public_key ):
    try :
        public_key.verify(
        signature ,
        message.encode(),
       padding.PSS (
            mgf = padding.MGF1(hashes.SHA256()),
            salt_length= padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
       )
        print("valid signature")
    except:
        print ("invalid signature")

#____________________________________________________
#.................3.Password protection...............

def hash_password(password):
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt , 
        1000000
    )
    return salt + pw_hash

def verfiy_password (stored_password , recived_password):
    #exract the salt (first 16 bit )
    salt = stored_password[:16]
    #extract the stred hash 
    stored_hash = stored_password[16:]
    #make the salt for the recived password 
    new_hash  = hashlib.pbkdf2_hmac(
        'sha256',
        recived_password.encode(),
        salt ,
        100000

    )
    return hashlib.compare_digest (stored_hash , new_hash)



if __name__ == "__main__":
    key = secrets.token_bytes(32)
    massge1 = input("Enter the meassage : ")
    mac_tag = mac_gen(massge1,key)
    print(mac_tag)
    message2 = input("Enter the second meassge to verfy :")
    print(verify_mac(message2 , mac_tag,key))
    private_key = rsa.generate_private_key(public_exponent = 65537  , key_size = 2048)
    public_key = private_key.public_key()
    sig = digiral_signature_genrateenhased(massge1,private_key)
    massage_to_check_ds = input("Enter the massage to verfiy digital signature")
    is_valid = verify_signature(massage_to_check_ds , sig , public_key)
    print(is_valid)

    user_password = input("enter your password please to protect it  : ") 
    hashed_db_value = hash_password(user_password)
    input_pass = input("enter your password to detect :")
    if verfiy_password(user_password,input_pass):
        print("Entering successful , the passowd is correct ")
    print("wrong password ")

   
