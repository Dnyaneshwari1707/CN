import math,pyperclip

from tkinter import *
from tkinter import scrolledtext

dict1 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
         'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

dict2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
         5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
         10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
         15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
         20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

# Key values
a = 17
b = 20


# Funtion to encrypt message
def affine_Encrypt(msg):
    cipher = ''
    for letter in msg:
        if letter == ' ':
            cipher += ' '
        else:
            z = (a*dict1[letter] + b) % 26
            cipher += dict2[z]



    window = Tk()
    window.title("Affine Encrypt ")
    window.geometry('600x350')
    txt = scrolledtext.ScrolledText(window,width=50,height=20,font=("Arial Bold", 15))
    txt.grid(column=0,pady = 10, padx = 20)
    txt.insert(INSERT,'\n\t\t  Affine cipher \n\n\tIt uses modular arithmetic to transform the integer that each plaintext letter corresponds to into another integer that correspond to a ciphertext letter. The encryption function for a single letter is  \n\tE ( x ) = ( a x + b ) mod m \n\tmodulus m: size of the alphabet\n\ta and b: key of the cipher.\n\ta must be chosen such that a and m are coprime.  ')
    txt.configure(state = 'disabled')
    window.mainloop()

    return cipher


# Funtion to decrypt cipher
def affine_Decrypt(cipher):
    message = ''
    a_inv = 0
    flag = 0
    # Find a^-1, the multiplicative inverse of a
    # in the group of integers modulo m.
    # Here m=26
    for i in range(26):
        flag = (a*i) % 26
        if flag == 1:
            a_inv = i
            break

    for letter in cipher:
        if letter == ' ':
            message += ' '
        else:
            z = (a_inv*(dict1[letter]-b)) % 26
            message += dict2[z]

    window = Tk()
    window.title("Affine Decrypt ")
    window.geometry('600x350')
    txt = scrolledtext.ScrolledText(window,width=50,height=20,font=("Arial Bold", 15))
    txt.grid(column=0,pady = 10, padx = 20)
    txt.insert(INSERT,'\n\t\t Affine cipher \n\n\tIn deciphering the ciphertext, we must perform the opposite (or inverse) functions on the ciphertext to retrieve the plaintext. Once again, the first step is to convert each of the ciphertext letters into their integer values. The decryption function is  \n\tD ( x ) = a^-1 ( x - b ) mod m\n\ta^-1 : modular multiplicative inverse of a modulo m. i.e., it satisfies the equation\n\t1 = a a^-1 mod m .  ')
    txt.configure(state = 'disabled')
    window.mainloop()    

    return message


keyword = "strawberries"
alphabet = "abcdefghijklmnopqrstuvwxyz"
def vigenere_encrypt(message):
	index = 0
	keyword_phrase = ""
	coded_message = ""

	for char in message:
		
		# Deal with non-alphabet characters
		if char not in alphabet:
			keyword_phrase = keyword_phrase + char
			coded_message = coded_message + char
			continue

		# Add keyword character to keyword_phrase
		keyword_phrase = keyword_phrase + keyword[index]

		# Shift message character by its keyword_phrase character
		charIndex = alphabet.find(char)
		keyIndex = alphabet.find(keyword[index])
		newIndex = charIndex + keyIndex

		if newIndex >= len(alphabet):
			newIndex = newIndex % len(alphabet)

		# Add character to coded message
		letter = alphabet[newIndex]
		coded_message = coded_message + letter

		# Update index
		index += 1
		if index >= len(keyword):
			index = index % len(keyword)

	window = Tk()
	window.title("Vigenere Decrypt ")
	window.geometry('600x350')
	txt = scrolledtext.ScrolledText(window,width=50,height=20,font=("Arial Bold", 15))
	txt.grid(column=0,pady = 10, padx = 20)
	txt.insert(INSERT,'\n\t\t Vigenère Cipher \n\n\tEncryption\n\tThe plaintext(P) and key(K) are added modulo 26.\n\tEi = (Pi + Ki) mod 26 \n\t Input : Plaintext :   GEEKSFORGEEKS\n\t            Keyword :  AYUSH\n\tOutput : Ciphertext :  GCYCZFMLYLEIM \n\tFor generating key, the given keyword is repeated in a circular manner until it matches the length of the plain text.  ')
	txt.configure(state = 'disabled')
	window.mainloop()

	return coded_message
    
def vigenere_decrypt(message):
	index = 0
	keyword_phrase = ""
	decoded_message = ""

	for char in message:
		
		# Deal with non-alphabet characters
		if char not in alphabet:
			keyword_phrase = keyword_phrase + char
			decoded_message = decoded_message + char
			continue

		# Add keyword character to keyword_phrase
		keyword_phrase = keyword_phrase + keyword[index]

		# Unshift message character by its keyword_phrase character
		charIndex = alphabet.find(char)
		keyIndex = alphabet.find(keyword[index])
		newIndex = charIndex - keyIndex

		if newIndex >= len(alphabet):
			newIndex = newIndex % len(alphabet)

		# Add character to decoded message
		letter = alphabet[newIndex]
		decoded_message = decoded_message + letter

		# Update index
		index += 1
		if index >= len(keyword):
			index = index % len(keyword)
	window = Tk()
	window.title("Vigenere Decrypt ")
	window.geometry('600x350')
	txt = scrolledtext.ScrolledText(window,width=50,height=20,font=("Arial Bold", 15))
	txt.grid(column=0,pady = 10, padx = 20)
	txt.insert(INSERT,'\n\t\t Vigenère Cipher \n\n\t Decryption\n\tDi = (Ei - Ki + 26) mod 26 \n\tInput : Ciphertext : GCYCZFMLYLEIM\n\t	Keyword :  AYUSH\n\tOutput : Decrypted Text : GEEKSFORGEEKS\n\tFor generating key, the given keyword is repeatedin a circular manner until it matches the length of the plain text.  ')
	txt.configure(state = 'disabled')
	window.mainloop()
	return decoded_message    

key = "KEY"
  
# Encryption
def col_trans_encrypt(msg):
    cipher = ""
  
    # track key indices
    k_indx = 0
  
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
  
    # calculate column of the matrix
    col = len(key)
      
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
  
    # add the padding character '_' in empty
    # the empty cell of the matix 
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
  
    # create Matrix and insert message and 
    # padding characters row-wise 
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
  
    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] 
                          for row in matrix])
        k_indx += 1

    window = Tk()
    window.title("col_trans_encrypt ")
    window.geometry('600x350')
    txt = scrolledtext.ScrolledText(window,width=50,height=20,font=("Arial Bold", 15))
    txt.grid(column=0,pady = 10, padx = 20)
    txt.insert(INSERT,'\n\t       Columnar Transposition Cipher \n\n   In a Transposition Cipher, the order of the alphabets is \n   re-arranged to obtain the cipher-text. \n\n     "The Columnar Transposition Cipher" is a form of                                     transposition cipher. \n -> It involves writing the plaintext out in rows, and then         reading the ciphertext off in columns one by one. \n -> It involves the use of a "keyword", which is used to           read out the message in the form of columns,                    (in alphabetical order). \n -> Any spare spaces are filled with nulls or left blank or         placed by a character ( _ )\n\n  Example \n\t\t * * *  Encryption * * *  \n\t   Input : Geeks for Geeks\n\t   Key = HACK\n\t   Output : e  kefGsGsrekoe_\n\n\t\t * * * Decryption * * * \n\t   Input : e  kefGsGsrekoe_\n\t   Key = HACK\n\t   Output : Geeks for Geeks  ')
    txt.configure(state = 'disabled')
    window.mainloop()
  
    return cipher
  
# Decryption
def col_trans_decrypt(cipher):
    msg = ""
  
    # track key indices
    k_indx = 0
  
    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
  
    # calculate column of the matrix
    col = len(key)
      
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
  
    # convert key into list and sort 
    # alphabetically so we can access 
    # each character by its alphabetical position.
    key_lst = sorted(list(key))
  
    # create an empty matrix to 
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
  
    # Arrange the matrix column wise according 
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
  
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
  
    # convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
  
    null_count = msg.count('_')
  
    if null_count > 0:
        return msg[: -null_count]

    window = Tk()
    window.title("col_trans_encrypt ")
    window.geometry('600x350')
    txt = scrolledtext.ScrolledText(window,width=50,height=20,font=("Arial Bold", 15))
    txt.grid(column=0,pady = 10, padx = 20)
    txt.insert(INSERT,'\n\t       Columnar Transposition Cipher \n\n   In a Transposition Cipher, the order of the alphabets is \n   re-arranged to obtain the cipher-text. \n\n     "The Columnar Transposition Cipher" is a form of                                     transposition cipher. \n -> It involves writing the plaintext out in rows, and then         reading the ciphertext off in columns one by one. \n -> It involves the use of a "keyword", which is used to           read out the message in the form of columns,                    (in alphabetical order). \n -> Any spare spaces are filled with nulls or left blank or         placed by a character ( _ )\n\n  Example \n\t\t * * *  Encryption * * *  \n\t   Input : Geeks for Geeks\n\t   Key = HACK\n\t   Output : e  kefGsGsrekoe_\n\n\t\t * * * Decryption * * * \n\t   Input : e  kefGsGsrekoe_\n\t   Key = HACK\n\t   Output : Geeks for Geeks  ')
    txt.configure(state = 'disabled')
    window.mainloop()
  
    return msg

def caesar_encrypt(message, shift):
    cipher = ''
    for letter in message:
        # checks for space
        if(letter != ' '):
            # looks up the dictionary and adds the shift to the index
            num = (dict1[letter] + shift) % 26
            # looks up the second dictionary for the
            # shifted alphabets and adds them
            cipher += dict2[num]
        else:
            # adds space
            cipher += ' '

    window = Tk()
    window.title("caesar_encrypt ")
    window.geometry('600x350')
    txt = scrolledtext.ScrolledText(window,width=50,height=20,font=("Arial Bold", 15))
    txt.grid(column=0,pady = 10, padx = 20)
    txt.insert(INSERT,'\n\t\t Caesar cipher \n\n\t The Caesar cipher is a kind of replacement (substitution) cipher, where all letter of plain text is replaced by another letter.\n\t The formula of encryption is:\n\tEn (x) = (x + n) mod 26 \n\t Text : ATTACKATONCE\n\t\tShift: 4\n\tCipher: EXXEGOEXSRGI')
    txt.configure(state = 'disabled')
    window.mainloop() 
    
    return cipher

def caesar_decrypt(message, shift):
    decipher = ''
    for letter in message:
        # checks for space
        if(letter != ' '):
            # looks up the dictionary and subtracts the shift to the index
            num = (dict1[letter] - shift + 26) % 26
            # looks up the second dictionary for the
            # shifted alphabets and adds them
            decipher += dict2[num]
        else:
            # adds space
            decipher += ' '

    window = Tk()
    window.title("caesar_decrypt ")
    window.geometry('600x350')
    txt = scrolledtext.ScrolledText(window,width=50,height=20,font=("Arial Bold", 15))
    txt.grid(column=0,pady = 10, padx = 20)
    txt.insert(INSERT,'\n\t\t Caesar cipher\n\n\t The Caesar cipher is a kind of replacement (substitution) cipher, where all letter of plain text is replaced by another letter.\n\t The formula of decryption is:\n\tDn (x) = (xi - n) mod 26\n\n\tIf any case (Dn) value becomes negative (-ve), in this case, we will add 26 in the negative value.  ')
    txt.configure(state = 'disabled')
    window.mainloop()
    
    return decipher


def autokey_encrypt(message,key_new):
    cipher_text = ''
    i = 0
    for letter in message:
        if letter == ' ':
            cipher_text += ' '
        else:
            x = (dict1[letter]+dict1[key_new[i]]) % 26
            i += 1
            cipher_text += dict2[x]

    window = Tk()
    window.title("autokey_encrypt ")
    window.geometry('600x350')
    txt = scrolledtext.ScrolledText(window,width=50,height=20,font=("Arial Bold", 15))
    txt.grid(column=0,pady = 10, padx = 20)
    txt.insert(INSERT,'\n\t\t Autokey cipher\n\n Lets explain Example 1:\n\tGiven plain text is : H E L L O\n\tKey is              : N H E L L\n\tLets encrypt:\n\tPlain Text(P)       : H   E   L   L   O\n\tCorresponding Number: 7   4   11  11  14     \n\tKey(K)              : N   H   E   L   L\n\tCorresponding Number: 13  7   4   11  11      \n\t                    ---------------------\n\tApplying the formula: 20  11  15  22  25  \n\tCorresponding \n\tLetters are         : U    L   P   W   Z\n\tHence Ciphertext is: ULPWZ  ')
    txt.configure(state = 'disabled')
    window.mainloop()

    return cipher_text

# This function decrypts the encrypted text
# and returns the original text
def autokey_decrypt(cipher_text,key_new):
    or_txt = ''
    i = 0
    for letter in cipher_text:
        if letter == ' ':
            or_txt += ' '
        else:
            x = (dict1[letter]-dict1[key_new[i]]+26) % 26
            i += 1
            or_txt += dict2[x]

    window = Tk()
    window.title("autokey_decrypt ")
    window.geometry('600x450')
    txt = scrolledtext.ScrolledText(window,width=50,height=20,font=("Arial Bold", 15))
    txt.grid(column=0,pady = 10, padx = 20)
    txt.insert(INSERT,'\n\t\t Autokey cipher\n\n Lets explain Example 1:\n\tGiven plain text is : H E L L O\n\tKey is              : N H E L L\n\tLets encrypt:\n\tPlain Text(P)       : H   E   L   L   O\n\tCorresponding Number: 7   4   11  11  14     \n\tKey(K)              : N   H   E   L   L\n\tCorresponding Number: 13  7   4   11  11      \n\t                    ---------------------\n\tApplying the formula: 20  11  15  22  25  \n\tCorresponding \n\tLetters are         : U    L   P   W   Z\n\tHence Ciphertext is: ULPWZ  ' )
    txt.configure(state = 'disabled')
    window.mainloop()
    
    return or_txt





