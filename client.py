from tkinter import *
import socket
from tkinter.ttk import Combobox
from encrypt import vigenere_encrypt
from encrypt import affine_Encrypt 
from encrypt import col_trans_encrypt
from encrypt import caesar_encrypt
from encrypt import autokey_encrypt

root = Tk()
root.title('Client')
root.geometry("1500x600")
bg = PhotoImage(file = "image2.png")
  
# Create Canvas
canvas1 = Canvas( root, width = 1500,height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

file_name = StringVar()
btn = StringVar()
encrypted = StringVar()


text = Text(root,height=30,width=500,font=("Arial Bold", 18))
try:  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    text.insert(INSERT,"\n\t\t\t\t\t Socket created successfully!\n")
except socket.error as err:  
    text.insert(INSERT,"\tsocket creation failed with error %s\n" %(err))

port = 8080
try:  
    s.connect(('127.0.0.1', port)) 
    text.insert(INSERT,"\n\t\t\t\t\t Connected to server!\n") 
except socket.error as err:  
    text.insert(INSERT,"Connection error :  %s\n" %(err))

label = Label(root,text = '  ***  Cryptography  *** ',font=("Arial Bold", 25),bg = "light green")
label.place(x=600,y=50)


label = Label(root,text = 'Enter filename : ',font=("Arial Bold", 25),fg = "blue",bg = "light green")
label.place(x=320,y=150)
file_entry = Entry(root,font=("Arial ", 25),bg = "light blue")
file_entry.place(x=620,y=150)


label = Label(root,text = 'Select the appropriate choice: ',font=("Arial", 25),fg = "blue",bg = "light blue")
label.place(x=320,y=220)
rdbtn1 = Radiobutton(root,text='Encryption',value='E',variable = btn,font=("Arial", 25),fg = "blue",bg = "yellow")
rdbtn1.place(x=790,y=250)
rdbtn2 = Radiobutton(root,text='Decryption',value='D',variable = btn,font=("Arial", 25),fg = "blue",bg = "yellow")
rdbtn2.place(x=1000,y=250)

label = Label(root,text = 'Select the type of encryption: ',font=("Arial Bold", 25),fg = "blue",bg = "light green")
label.place(x=320,y=320)
data=("1. Vigenere Cipher ","2.Affine Cipher ","3. Col_trans Cipher ","4.Caeser Cipher ","5. Autokey Cipher ")
cb=Combobox(root, values=data,width = 30,font=("Arial", 25))
cb.place(x=800, y=370)

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

def execute() :
    fname = file_entry.get()
    s.send(bytes(fname,'utf-8'))

    print("Filename is ",fname)
    f = open(fname)
    msg = f.readline()
    f.close()
    print("Message :",msg)

    pr = btn.get()
    print("Choice : ",pr)
    s.send(bytes(pr,'utf-8'))

    choice = cb.get()
    ch = choice[0]
    print("Choice selected is ",ch)
    s.send(bytes(ch,'utf-8'))

    if ch == '1' :
        if pr == 'E':
            encrypted = vigenere_encrypt(msg)
            
        elif pr == 'D':
            encrypted = msg
    if ch == '2' :
        if pr == 'E':
            encrypted = affine_Encrypt(msg)
        elif pr == 'D':
            encrypted = msg
    if ch == '3' :
        if pr == 'E':
            encrypted = col_trans_encrypt(msg)
        elif pr == 'D':
            encrypted = msg

    if ch == '4' :
        if pr == 'E':
            encrypted = caesar_encrypt(msg, 13)
        elif pr == 'D':
            encrypted = msg

    if ch == '5' :
        if pr == 'E':
            key = 'NEW'
            key_new = generate_key(msg, key)
            encrypted = autokey_encrypt(msg,key_new)
        elif pr == 'D':
            encrypted = msg
            
    print("Encrypted Cipher : ",encrypted)
    s.send(bytes(encrypted,'utf-8'))
    


submit_button = Button(root,text = 'Submit',command = execute,font=("Arial", 25),bg='yellow',activebackground='blue')
submit_button.place(x=320,y=420)
text.pack()
mainloop()
s.close()


