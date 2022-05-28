import ast
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#Generating Key
key = RSA.generate(1024)

#Storing Public key in file named as my_rsa_public .pem
f=open('my_rsa_public.pem','wb')
f.write (key.publickey().exportKey("PEM"))
f.close()

#Storing Private key in file named as my_rsa_private.pem
f = open('my_rsa_private.pem','wb')
f.write(key.export_key('PEM'))
f.close()

#Encryption
f = open('my_rsa_public.pem', 'rb')
key=RSA.importKey(f.read())
message = input("Enter message to Encrypt: ")
encryptor = PKCS1_OAEP.new(key)
encrypted = encryptor.encrypt (bytes (message, 'utf-8'))
print("Encrypted message is", encrypted)

#Decryption
fl = open('my_rsa_private.pem','rb')
keyl = RSA.importKey(fl.read())
message=input("Enter encrypted message to Decrypt: ")

decryptor = PKCS1_OAEP.new(keyl)
decrypted = decryptor.decrypt(ast.literal_eval(str(message)))
print (decrypted)
