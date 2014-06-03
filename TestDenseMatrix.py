## File: TestDenseMatrix.py
## Description: Part 1 Matrix is represented as 2-D list
##              implement the __str__() function that will return a 2-D representation of
##              the matrix with the numbers in neat columns right justified with any number
##              of digits.
## Author: Xiaoqin LI
## Date Created: 03/28/2014
## Date Last Modified:04/04/2014

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = []

  # performs a matrix addition
  def __add__ (self, other):
    if ((self.row != other.row) or (self.col != other.col)):
      return None

    mat = Matrix(self.row, self.col)
    for i in range (self.row):
      new_row = []
      for j in range (self.col):
        new_row.append (self.matrix[i][j] + other.matrix[i][j])
      mat.matrix.append(new_row)

    return mat

  # performs a matrix multiplication
  def __mul__ (self, other):
    if (self.col != other.row):
      return None

    mat = Matrix (self.row, other.col)
    for i in range (self.row):
      new_row = []
      for j in range (other.col):
        sum = 0
        for k in range (other.row):
          sum = sum + self.matrix[i][k] * other.matrix[k][j]
        new_row.append (sum)
      mat.matrix.append (new_row)

    return mat

  # get max digits length of matrix
  def max_digit_length(self):
    max_length = 1
    for row in range(self.row):
        for col in range(self.col):
          if len(str(self.matrix[row][col]))> max_length:
                 max_length = len(str(self.matrix[row][col]))
    return max_length
  
  # returns a string representation of the matrix
  # print Matrix in proper format
  def __str__ (self):
    digit_length = self.max_digit_length()                        
    s = ''
    for row in range(self.row):
        for col in range(self.col):
            temp_str = str(self.matrix[row][col])
            s += temp_str.rjust(digit_length)
            s += ' '
        s += '\n'
    return s
                                  
def readMatrix(inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int(line[0])
  col = int(line[1])
  mat = Matrix(row, col)

  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    for j in range (col):
      line[j] = int(line[j])
    mat.matrix.append(line)
  line = inFile.readline()
  
  return mat

def main():
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

  inFile.close()

main()
