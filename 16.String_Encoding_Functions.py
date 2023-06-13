
import base64

'''base64 module : It contains functions for encoding and decoding  the binary data to printable ASCII form'''
Str = 'Hello all! This is python learner 2041'

#encryption
enStr = base64.b64encode(Str.encode('utf-8'))
print('The encoded form of the String Str is : ',enStr)

#decryption
deStr = base64.b64decode(enStr.decode('utf-8'))
print('The decoded form of the String Str is : ',deStr)