import socket
from encrypt import vigenere_decrypt
from encrypt import affine_Decrypt
from encrypt import col_trans_decrypt
from encrypt import caesar_decrypt
from encrypt import autokey_decrypt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

port = 8080
s.bind(('', port)) 
s.listen(5)
c,addr = s.accept()


recv = c.recv(1024)
fname = recv.decode('utf-8')
print("Filename : ",fname)

recv = c.recv(1024)
pr = recv.decode('utf-8')
print("Ch : ",pr)

recv = c.recv(1024)
ch = recv.decode('utf-8')
print("Choice: ",ch)

recv = c.recv(1024)
msg = recv.decode('utf-8')
print("Message Received : ",msg)

def generate_key(message, key):
    i = 0
    while True:
        if len(key) == len(message):
            break
        if message[i] == ' ':
            i += 1
        else:
            key += message[i]
            i += 1
    print("Key is : ", key)
    return key

if pr == 'E':
    result = msg
elif pr == 'D':
    if ch == '1':
        result = vigenere_decrypt(msg)
        
if pr == 'E':
    result = msg
elif pr == 'D':
    if ch == '2':
        result = affine_Decrypt(msg)
        
if pr == 'E':
    result = msg
elif pr == 'D':
    if ch == '3':
        result = col_trans_decrypt(msg)
        
if pr == 'E':
    result = msg
elif pr == 'D':
    if ch == '4':
        result = caesar_decrypt(msg, 13)
        
if pr == 'E':
    result = msg
elif pr == 'D':
    if ch == '5':
        key = 'NEW'
        key_new = generate_key(msg, key)
        result = autokey_decrypt(msg,key_new)
    
    print("Decrypted Cipher : ",result)
        


f = open(fname,'w')
f.write(result)
f.close()
c.close()

