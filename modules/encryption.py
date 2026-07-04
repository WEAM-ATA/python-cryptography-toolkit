import secrets 
from cryptography.hazmat.primitives.ciphers.aead import AESGCM 
from cryptography.hazmat.primitives.asymmetric import rsa , padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization 


# symmetric function 
def aes_ed(massage):
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)
    aes = AESGCM(key)

    ciphertext = nonce + aes.encrypt(nonce , massage.encode() , None)
    plaintext = aes.decrypt(ciphertext[:12] , ciphertext[12:], None)

    return key.hex() , ciphertext.hex() , plaintext.decode(), nonce.hex() ,aes


#Asymmetric function 

def rsa_ed(message):
    private_key = rsa.generate_private_key(public_exponent = 65537  , key_size = 2048)
    public_key = private_key.public_key()

    # to display private and public keys 
    private_pem = private_key.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.PKCS8,
        encryption_algorithm= serialization.NoEncryption()
    ).decode()

    public_pem = public_key.public_bytes(
        encoding= serialization.Encoding.PEM,
        format= serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

    #ecryption 
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP (
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm= hashes.SHA256(),
            label=None
        )
    )

    #decrytion
    plaintext = private_key.decrypt(
        ciphertext ,
        padding.OAEP(
            mgf= padding.MGF1(algorithm=hashes.SHA256()),
            algorithm= hashes.SHA256(),
            label=None
        )
    )
    return private_pem , public_pem , ciphertext.hex() , plaintext.decode() , 

    




if __name__ == "__main__":
    print(aes_ed("Hello AES !"))
    print(rsa_ed("Hello , RSA !"))




