## File: BST_Cipher.py
## Description:  we will create a simple
##              encryption scheme using a binary search tree. To encode
##              a sentence, insert each letter into a binary tree using
##              the ASCII value as a comparative measure. 
## Author: Xiaoqin LI
## Date Created: 04/18/2014
## Date Last Modified:04/20/2014


class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
        for char in encrypt_str:
            self.insert(char)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        if ch.isalpha() or ch == " ":
            newNode = Node(ch)
            if (self.root == None):
                self.root = newNode
            else:
                if not self.check_duplicates(ch):
                    current = self.root
                    parent = self.root
                    while (current != None):
                        parent = current
                        if (ch < current.data):
                            current = current.lChild
                        else:
                            current = current.rChild
                    if (ch < parent.data):
                        parent.lChild = newNode
                    else:
                        parent.rChild = newNode
                
    # A helper function for insert function.
    # If the character already exists, it does not add that character.
    def check_duplicates(self,ch):
        current = self.root
        while ((current != None) and (current.data != ch)):
            if (ch < current.data):
                current = current.lChild
            else:
                current = current.rChild
        return current
   
    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        if not self.check_duplicates(ch):
            return ""
        else:
            current = self.root
            if ch == current.data:
                return "*"
            else:
                string = ""
                while ((current != None) and (current.data != ch)):
                    if (ch < current.data):
                        current = current.lChild
                        string += "<"
                    else:
                        current = current.rChild
                        string += ">"
                return string
            
    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        current = self.root
        if st == "*":
            return self.root.data
        for entry in st:
            if current != None:
                if entry == "<":
                    current = current.lChild
                elif entry == ">":
                    current = current.rChild
            else:
                return ""
        return current.data

    # the encrypt() function takes a string as input parameter, convert
    # it to lower case, and returns the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        target_str= ""
        st = st.lower()
        for entry in st:
            if entry.isalpha() or entry == " ":
                target_str += entry
        encrypted_str = ""
        for entry in target_str:
            current_encrypted = self.search(entry)
            encrypted_str +=current_encrypted + "!"
            
        return encrypted_str[0:-1]
            
    # the decrypt() function takes a string as input parameter, and
    # returns the decrypted string.
    def decrypt (self, st):
        raw_str =  ""
        for entry in st:
            if entry == ">" or entry == "<" or entry == "!" or entry == "*":
                raw_str+=entry       
        str_list = raw_str.split('!')
        decrypted_str = ""
        for entry in str_list:       
            decrypted_str += self.traverse(entry)
        return decrypted_str

def main():
    encryption_key = input("Enter encryption key: ")  # Enter the key
    encryption_key = encryption_key.lower()
    key_tree = Tree(encryption_key)
    print()
    encrypting_str = input("Enter string to be encrypted: ") # Enter the encrypting string
    encrypted_str = key_tree.encrypt(encrypting_str)
    print("Encrypted string: ", encrypted_str)
    print()
    decripting_str = input("Enter string to be decrypted: ") # Enter the decrypting string
    decrypted_str = key_tree.decrypt(decripting_str)
    print("Decrypted string: ",decrypted_str)
main()



