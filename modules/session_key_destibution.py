import secrets 
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa , padding 
from cryptography.hazmat.primitives import hashes


#session key destripution 

def skd(key , message):
    nonce = secrets.token_bytes(12)
    eas = AESGCM(key)

    #generate the RSA private abd public keys  
    private_key = rsa.generate_private_key(public_exponent= 65537 , key_size= 2048)
    public_key = private_key.public_key()
    ss = eas


    #encrypt the key using the public key 
    enc_key = public_key.encrypt(
        key ,
        padding.OAEP(
            mgf= padding.MGF1(algorithm= hashes.SHA256()),
            algorithm= hashes.SHA256(),
            label=None

        )       
    )
    dec_key = private_key.decrypt(
        enc_key , 
        padding.OAEP(
            mgf = padding.MGF1(algorithm= hashes.SHA256()),
            algorithm= hashes.SHA256(),
            label=None 
        )
    )

    #encrypt the message using session key 

    ciphertext = nonce + eas.encrypt(nonce , message.encode(),None)
    plaintext = eas.decrypt(ciphertext[:12], ciphertext[12:], None)
    return {"the encrypted Key using public key is ": enc_key.hex() ,"the decrypted key key using private key is ": dec_key.hex(),
            "the encrypted message " : ciphertext.hex(),
            "the plaintext ": plaintext} 



if __name__ =="__main__":
    key = secrets.token_bytes(32)
    m = input("Enter message : ")
    print(skd(key,m))





