#DES implementaton using pyDes pure python.
import pyDes
import time

start_time = time.time()
# For Python3, you'll need to use bytes, i.e.:
#   data = b"Please encrypt my data"
#   k = pyDes.des(b"DESCRYPT", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
f=open("5 MB.txt", "r")
if f.mode == 'r':
    data = f.read()
#data = b"Please encrypt my data"
k = pyDes.des(b"DESCRYPT", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)
print("Encrypted: %r" % d)
print("--- %s seconds" % (time.time() - start_time))
#print("Decrypted: %r" % k.decrypt(d))

assert k.decrypt(d) == data