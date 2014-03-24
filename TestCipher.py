# File:  TestCipher.py
# Description: For the purposes of this programming project convert the message that you are asked
#              to encode or decode to lower case(Upper cases will be converted to lower case before
#              encoding or decoding). You will only be encoding or decoding the letters of the alphabet.
#              Punctuation marks and numerals remain untouched. 
#              The updated version of second assignment. Called four functions to encode and decode.
#              The results satisfies the requirement.Total time consumed: 110 minutes
# Author: Xiaoqin LI
# Date Created: 01/21/2014
# Date Last Modified: 01/24/2014

## Substitution Ciphering and Deciphering 
def substitution_encode ( plain_string ):
    cipher_str = 'q a z w s x e d c r f v t g b y h n u j m i k o l p'
    cipher = cipher_str.split()                             # Save the Cipher letters in a list of characters
    encoded_string = ''                                     # initializing encoded_string as an empty string
    for char in plain_string:
        if  char.isalpha():                                 # if the char is alphabet case, encode it
            if char.isupper():                              # if the letter is upper case, change it to lower case
                char = char.lower()
            idx = ord(char) - ord('a')                      # ciphering method for substitution encode
            encoded_string += cipher[idx]
        else:
            encoded_string += char                          # any chars other than alphabet remain untouched
    print ("Encoded Text: " + encoded_string)  

def substitution_decode ( encoded_str ):
    cipher_str = 'q a z w s x e d c r f v t g b y h n u j m i k o l p'
    cipher = cipher_str.split()
    plain_string = ''
    for char in encoded_str:
        if  char.isalpha():                                 # if the char is alphabet case, decode it
            if char.isupper():                          
                char = char.lower()
            ord_plain_char = ord('a') + cipher.index(char)  # deciphering method for substitution encode
            plain_string += chr(ord_plain_char)
        else:
            plain_string += char                        
    print ("Decoded Plain Text: " + plain_string)

## Vigenere Ciphering and Deciphering    
def vigenere_encode ( plain_string, passwd ):
    alphabet_base = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split() # create a alphabet base
    pwd_length = len(passwd)                                # get length of password
    current_index_plain_low = 0                             # initializing current index of only low case letters in plain string
    vigenere_encoded_string = ''
    for i in range(len(plain_string)):                  
        if plain_string[i].isalpha():                       # if the char is alphabet case, encode it
            if plain_string[i].isupper():
                lower_current_plain = plain_string[i].lower()                        # if the letter is capital, change it to lower case
            else:
                lower_current_plain = plain_string[i]
            index_plain_inbase = alphabet_base.index(lower_current_plain)            # get the index of current letter in plain string in alphabet base
            current_index_passwd = current_index_plain_low % pwd_length              # get the index of letter in password used to cipher
            current_index_plain_low += 1                                             # move to the next letter in plain string for next calculation of current_index_passwd
            index_passwd_inbase = alphabet_base.index(passwd[current_index_passwd])  # index for current passwd letter in  alphabetbase
            vigenere_encoded_index = (index_passwd_inbase + index_plain_inbase) % 26 # according to Vigenere Ciphering, index for current encoded letter in alphabet base is
                                                                                     # the sum of index of the letter in passowrd and the letter in plain string.
            vigenere_encoded_string += alphabet_base[vigenere_encoded_index]         # get the encoded letter
        else:
            vigenere_encoded_string += plain_string[i]                              
    print ("Encoded Text: " + vigenere_encoded_string) 

def vigenere_decode ( encoded_string, passwd ):           
    alphabet_base = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    pwd_length = len(passwd)
    current_index_encoded_low = 0                                                    # initializing current index of only low case letters in encoded string
    vigenere_decoded_string = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isalpha():
            if encoded_string[i].isupper():
                lower_current_encoded = encoded_string[i].lower()
            else:
                lower_current_encoded = encoded_string[i]
            current_index_passwd = current_index_encoded_low % pwd_length
            current_index_encoded_low += 1                                           # move to the next letter in encoded string for next calculation of current_index_passwd
            index_passwd_inbase = alphabet_base.index(passwd[current_index_passwd])
            index_encoded_inbase = alphabet_base.index(lower_current_encoded)        # get index for encoded letter in alphabet base
            if index_encoded_inbase < index_passwd_inbase:                           # calculate index of current decoded letter, wrapping the index of encoded letters if index of letter
                                                                                     # in passward is greater than it.
                index_plain_inbase = index_encoded_inbase + len(alphabet_base) - index_passwd_inbase
            else:
                index_plain_inbase = index_encoded_inbase - index_passwd_inbase
            vigenere_decoded_string += alphabet_base[index_plain_inbase]
        else:
            vigenere_decoded_string += encoded_string[i]
    print ("Decoded Plain Text: " + vigenere_decoded_string) 

## main()    
def main():                                                 # giving the inputs and calling each function
    print("Substitution Cipher")
    print()
    plain_str = input("Enter Plain Text to be Encoded: ")
    substitution_encode(plain_str)
    print()    
    encoded_str = input("Enter Encoded Text to be Decoded: ")
    substitution_decode(encoded_str)
    print()
    
    print("Vigenere Cipher")
    print()
    vigenere_plain_str = input("Enter Plain Text to be Encoded: ")
    pass_phrase1 = input("Enter Pass Phrase (no spaces allowed): ")
    vigenere_encode ( vigenere_plain_str, pass_phrase1 )
    print()
    vigenere_encoded_str = input("Enter Encoded Text to be Decoded: ")
    pass_phrase2 = input("Enter Pass Phrase (no spaces allowed): ")
    vigenere_decode ( vigenere_encoded_str, pass_phrase2 )
    
main()
