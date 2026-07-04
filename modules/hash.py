import hashlib 

def hash_text(message):
   h = hashlib.sha256(message.encode())
   hashdigest = h.digest()
   return (hashdigest.hex())
   



def hash_file(file_path):
    #using SHA256 for hashing 
    h = hashlib.new("sha256")
    #read the file as bytes due to hash algorithim understand only bytes
    with open(file_path , "rb") as file :
        while True :
         #read the file as chunks if it is large 
         chunk = file.read(1024)
         #the while loop executed until file is empty 
         if chunk == b"":
            break
         #update the every new chunk to the complete hash object 
         h.update(chunk)
    #return the result in hexidecemal to be readable 
    return h.hexdigest()

# useful usage 
def verify_integrity(f1, f2):
   #using the hash_file function to get hash values to both files 
   hash1 = hash_file(f1)
   hash2 = hash_file(f2)
   print("/n checking the integrty between: "+ f1 + f2  )
   #check if the both file have the same Hash vlaue 
   if hash1 == hash2:
      return "no modifiction has been made"
   return "the file has been modified .Possibly unsafe "





if __name__ == "__main__":
   print("the SHA hash for the file is :" + hash_file(r"venv\sample\sample.txt"))
   print(verify_integrity(r"venv\sample\unnamed (11) - Copy - Copy.png", r"venv\sample\unnamed (11).jpg"))
   message = "Hello."
   print("the hased message is : " , hash_text(message))
   

