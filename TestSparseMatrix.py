##  File: TestSparseMatrix.py
##  Description: Part 2 Sparse matrix representation has a single linked list having the row,
##              column, and non-zero data in each link. Matrix is represented as 2-D list            
##              implement the __str__() function that will return a 2-D representation of
##              the matrix with the numbers in neat columns right justified with any number
##              of digits.
## Author: Xiaoqin LI
## Date Created: 03/28/2014
## Date Last Modified:04/04/2014

class Link (object):
  def __init__ (self, row = 0, col = 0, data = 0, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = next

  # returns a String representation of a Link (row, col, data)
  def __str__ (self):
    s = ''
    s += str(self.row) + ' ' + str(self.col) + ' ' + str(self.data) + '\n'
    return s

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertLast (self, row, col, data):
    newLink = Link (row, col, data)
    current = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  # returns a String representation of a LinkedList
  def __str__ (self):
    s = ''
    current = self.first
    while current != None:
      s += str(current.data)
      s += ' '
      current = current.next
    return s

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = LinkedList()
  
  # finds the Link having row and col value
  def find (self, row, col):
    current = self.matrix.first
    while current != None:
      if current.col == col and current.row == row:
        return current
      current = current.next
    return None

  # removes the Link having row and col value
  def delete (self, row, col):
    current = self.matrix.first
    previous = self.matrix.first
    while current != None:
      if current.col == col and current.row == row:
        if current == self.matrix.first:
          self.matrix.first = self.matrix.first.next
        else:
          previous.next = current.next
        return current
      else:
        previous = current
        current = current.next
    return None

  def addFirst(self, row,col,data):
    newLink = Link(row, col, data)
    newLink.next = self.matrix.first
    self.matrix.first = newLink

  # Performs assignment operation:  matrix[row][col] = data
  def setElement (self, row, col, data):
    if col > self.col or row > self.row:
      return
    if data == 0:
      self.delete(row, col)
      return
    else:
      current = self.matrix.first
      previous = self.matrix.first
      newLink = Link(row,col,data)
      if current == None:
        self.addFirst(row, col, data)
        return
      else:
        while current != None:
          if row == current.row and col == current.col:
            current.data = data
            return
          else:
            if current.row < row:
              previous = current
              current = current.next
              continue
            if current.row == row:
              if current.col < col:
                previous = current
                current = current.next
                continue
              else: #current.col > col
                if previous.col < col:
                  previous.next = newLink
                  newLink.next = current
                  return
                else:
                  self.addFirst(row, col, data)
                  return            
            else:
              previous.next = newLink
              newLink.next = current
              return
        previous.next = newLink
        newLink.next = current
    
  # Adds two sparse matrices 
  def __add__ (self, other):    
    if (self.row != other.row) or (self.col != other.col):
      return None
    mat_add = Matrix(self.row, self.col)
    for i in range (self.row):
      for j in range (self.col):
        if self.find(i,j) == None and other.find(i,j) == None:
          continue
        elif self.find(i,j) != None and other.find(i,j) == None:
          found_link = self.find(i,j)
          mat_add.setElement(i,j,found_link.data)
        elif self.find(i,j) == None and other.find(i,j) != None:
          found_link = other.find(i,j)
          mat_add.setElement(i,j,found_link.data)
        elif self.find(i,j) != None and other.find(i,j) != None:
          found_link1 = self.find(i,j)
          found_link2 = other.find(i,j)
          current_data = found_link1.data + found_link2.data
          mat_add.setElement(i,j,current_data)
    return mat_add
          
  # Multiplies two sparse matrices 
  def __mul__ (self, other):
    if (self.col != other.row):
      return None
    mat_mul = Matrix (self.row, other.col)
    for i in range (self.row):
      for j in range (other.col):
        sum_ele = 0
        for k in range(self.col):
          ele_self = self.find(i,k)
          if ele_self == None:
            ele_self = 0
          else:
            ele_self = ele_self.data
          ele_other = other.find(k,j)
          if ele_other == None:
            ele_other = 0
          else:
            ele_other = ele_other.data
          sum_ele += ele_self*ele_other
        mat_mul.setElement(i,j,sum_ele)
    return mat_mul

  # Returns a linked list representing a row
  def getRow (self, n):
    linked_row = LinkedList()
    for i in range(self.row):
      if i < n:
        continue
      elif i == n:
        for j in range(self.col):
          if self.find(i,j) != None:
            current_link = self.find(i,j)
            linked_row.insertLast(i, j, current_link.data)
##          else:
##            linked_row.insertLast(i, j, 0)
      elif i > n:
        break
    return linked_row

  # Returns a linked list representing a column
  def getCol (self, n):
    linked_col = LinkedList()
    for i in range(self.row):
      for j in range(self.col):
        if j == n:
          if self.find(i,j) != None:
            current_link = self.find(i,j)
            linked_col.insertLast(i, j, current_link.data)
##          else:
##            linked_col.insertLast(i, j, 0)        
    return linked_col

  # get max digits length of matrix
  def max_digit_length(self):
    max_length = 1
    current_link = self.matrix.first
    while current_link != None:
      if len(str(current_link.data))> max_length:
        max_length = len(str(current_link.data))
      current_link = current_link.next
    return max_length
  
  # Returns a string representation of a matrix
  def __str__ (self):
    digit_length = self.max_digit_length()     
    s = ''
    current = self.matrix.first
    for i in range(self.row):
      for j in range(self.col):
        if current != None and current.row == i and current.col == j:
            temp_str = str(current.data)
            s += temp_str.rjust(digit_length)
            s += ' '
            current = current.next
        else:
          s += '0'.rjust(digit_length)
          s += ' '
      s = s[0:-1]
      s += '\n'  
    return s
  
# read in Matrix informations
def readMatrix (inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)
  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    for j in range (col):
      elt = int(line[j])
      if (elt != 0):
        mat.matrix.insertLast (i, j, elt)
  line = inFile.readline()
  return mat

def main ():
  inFile = open ("matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = readMatrix (inFile)
  print (matA)
  
  matB = readMatrix (inFile)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = readMatrix (inFile)
  print (matP)
  matQ = readMatrix (inFile)
  print (matQ)
  
  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.setElement (1, 1, 5)
  print (matA)

  print ("\nTest Getting a Row")
  row = matP.getRow(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.getCol(0)
  print (col)

  inFile.close()

main()

