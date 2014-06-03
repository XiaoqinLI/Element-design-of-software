#  File: TestPolynomial.py
#  Description: Sparse matrix representation has a single linked list
#               having the row, column, and non-zero data in each link
## Author: Xiaoqin LI

class Link (object):
  def __init__ (self, exp = 0, coe = 0,  next = None):
    self.coe = coe
    self.exp = exp   
    self.next = next

  # returns a String representation of a Link (row, col, data)
  def __str__ (self):
    s = ''
    s += str(self.coe) + 'x' + '^' + str(self.exp) + '\n'
    return s

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertLast (self, exp, coe):
    newLink = Link (exp, coe)
    current = self.first
    if coe == 0:
      return
    if (current == None):
      self.first = newLink
      return
    while (current.next != None):
      current = current.next
    current.next = newLink

  # returns a String representation of a Polynomial
  def __str__ (self):
    s = ''
    current = self.first
    while current != None:
      if current.coe != 0 and current.exp > 1:
        s += str(current.coe) + 'x^' + str(current.exp)
        s += '+'
      if current.coe != 0 and current.exp == 1:
        s += str(current.coe) + 'x'
        s += '+'
      if current.exp == 0:
        s += str(current.coe)
        s += '+'
      current = current.next
    if len(s) > 1:
      s = s[0:-1]
    return s
  
  # Adds two Polynomials
  def __add__(self, other):
    if (self.first == None) and (other.first == None) :
      return None
    elif (self.first != None) and (other.first == None) :
      return self
    elif (self.first == None) and (other.first != None) :
      return other
    else:
      poly_added = LinkedList()
      current_self = self.first
      current_other = other.first
      while (current_self != None and current_other != None):
        if current_self.exp == current_other.exp:
          poly_added.insertLast(current_self.exp,current_self.coe+current_other.coe)
          current_self = current_self.next
          current_other = current_other.next
        elif current_self.exp > current_other.exp:
          poly_added.insertLast(current_self.exp,current_self.coe)
          current_self = current_self.next
        else:
          poly_added.insertLast(current_other.exp,current_other.coe)
          current_other = current_other.next
      while (current_self!=None):
        poly_added.insertLast(current_self.exp,current_self.coe)
        current_self = current_self.next
      while (current_other!=None):
        poly_added.insertLast(current_other.exp,current_other.coe)
        current_other = current_other.next
    return poly_added
          
  # Multiplies two Polynomials 
  def __mul__ (self, other):
    if (self.first == None) and (other.first == None) :
      return None
    elif (self.first != None) and (other.first == None) :
      return self
    elif (self.first == None) and (other.first != None) :
      return other
    else:
      poly_mul = LinkedList()
      current_self = self.first
      current_other = other.first
      while (current_other != None):
        temp_list = LinkedList()
        while current_self != None:
          temp_exp = current_self.exp + current_other.exp
          temp_coe = current_self.coe * current_other.coe        
          temp_list.insertLast(temp_exp,temp_coe)
          current_self = current_self.next
        current_self = self.first
        poly_mul = poly_mul + temp_list
        current_other = current_other.next
    return poly_mul

def main ():
  A = ([3,4],[2,3],[1,2],[0,5])
  B = ([2,4],[1,3])
  print("poly1: ")
  poly1 = LinkedList()
  for entry in A:
    poly1.insertLast(entry[0],entry[1])
  print(poly1)
  print()
  print("poly2: ")
  poly2 = LinkedList()
  for entry in B:
    poly2.insertLast(entry[0],entry[1])
  print(poly2)
  print()
  print("poly1 + poly2")
  poly3 = poly1 + poly2
  print(poly3)
  print()
  print("poly1 * poly2")
  poly4 = poly1 * poly2
  print(poly4)
main()

