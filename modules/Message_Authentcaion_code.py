import hmac
import hashlib
import secrets

#HMAC FUNCTION 
def h_mac(message ,key):
    #using HMAC with SHA256
    h = hmac.new(key, message.encode(),hashlib.sha256)  
    return h.hexdigest()



if __name__ == "__main__":
    key = secrets.token_bytes(32)
    message = "Hello , HMAC"
    print("the HMAC for the message is " , h_mac(message , key)) 
