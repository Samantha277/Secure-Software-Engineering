from Crypto.Cipher import DES3
from Crypto import Random
import time

start_time = time.time()
f=open("5 MB.txt", "rb")
if f.mode == 'rb':
    plaintext = f.read()

key = 'Sixteen byte key'
iv = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)

#plaintext = b'sona si latine loqueri  ' #padded with spaces so than len(plaintext) is multiple of 8
encrypted_text = cipher_encrypt.encrypt(plaintext)
#print("Encrypted text is: ",encrypted_text)
#cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) #you can't reuse an object for encrypting or decrypting other data with the same key.
#print("Decrypted text is:  ",cipher_decrypt.decrypt(encrypted_text))
#cipher_decrypt.decrypt(encrypted_text) #you cant do it twice
print("--- %s seconds" % (time.time() - start_time))