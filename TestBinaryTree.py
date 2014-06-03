## File: TestBinaryTree.py
## Description: we will be adding to the classes Node and Tree that we developed in class
##              and testing them. There are several short methods that we will
##              have to write. We will create several trees and show convincingly
##              that our methods are working.
## Author: Xiaoqin LI
## Date Created: 04/10/2014
## Date Last Modified:04/12/2014


class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None
    
  # Search for a node with the key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)
    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lChild
        else:
          current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode
        
  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      self.inOrder(aNode.lChild)
      print(aNode.data)
      self.inOrder(aNode.rChild)

  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print(aNode.data)
      self.preOrder(aNode.lChild)
      self.preOrder(aNode.rChild)

  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder(aNode.lChild)
      self.postOrder(aNode.rChild)
      print(aNode.data)

  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent

  # Delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while ((deleteNode != None ) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lChild
        isLeft = True
      else:
        deleteNode = deleteNode.rChild
        isLeft = False
      
    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild != None): #go all the way to left in right sub tree
        successorParent = successor
        successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
        successor.rChild = deleteNode.rChild

    return True

  # Returns true if two binary trees are similar
  def isSimilar (self, self_pNode, Other_pNode):
    if self_pNode == None:
      return Other_pNode == None
    if Other_pNode == None:  # False if only one is None
      return False
    if self_pNode.data != Other_pNode.data: # False if data is not same
      return False
    # recursively check all Children.
    if self.isSimilar(self_pNode.lChild, Other_pNode.lChild) and \
       self.isSimilar(self_pNode.rChild, Other_pNode.rChild):
      return True
    return False
  
  # Prints out all nodes at the given level
  def printLevel (self, root, current_level):
    if current_level == 1:
      if root != None:
        print(root.data, end=" ")
        return
    else:
      if root != None:
        self.printLevel(root.lChild, current_level-1)
        self.printLevel(root.rChild, current_level-1)
      
  # Returns the height of the tree
  def getHeight (self, root):
    if root == None:
      return 0
    else:
      if root.lChild != None or root.rChild != None:
        return 1 + max(self.getHeight(root.lChild),self.getHeight(root.rChild))
      else:
        return 0
    
  # Returns the number of nodes in current sub tree
  def num_subtree_Nodes(self, root):
    if root == None:
      return 0
    else:
      return 1 + self.num_subtree_Nodes(root.lChild) + self.num_subtree_Nodes(root.rChild)
      
  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree
  def numNodes (self):
    if self.root != None:
      left_root = self.root.lChild
      right_root = self.root.rChild
      left_nodes_num = self.num_subtree_Nodes(left_root)
      right_nodes_num = self.num_subtree_Nodes(right_root)
      return left_nodes_num + right_nodes_num + 1
    else:
      return 0

    
def main():
  # Create two trees from input file
  infile = open("input.txt","r")
  
  tree1 = Tree()
  tree_node = infile.readline()
  while tree_node != '\n' and tree_node != "":
    tree_node = int(tree_node)
    tree1.insert(tree_node)
    tree_node = infile.readline()
    
  tree2 = Tree()
  tree_node = infile.readline()
  while tree_node != '\n' and tree_node != "":  
    tree_node = int(tree_node)
    tree2.insert(tree_node)
    tree_node = infile.readline()
    
  infile.close()
  
  # Test your method isSimilar()
  print(tree1.isSimilar(tree1.root, tree2.root))
  print()
  # Print  out all nodes at the various levels of two of the trees:
  # print levels 1, 3, and 5 of tree 1
  # print levels 2, 4, and 6 of tree 2
  print('level 1:', end= " ")
  tree1.printLevel(tree1.root,1)
  print()
  print('level 3:', end= " ")
  tree1.printLevel(tree1.root,3)
  print() 
  print('level 5:', end= " ")
  tree1.printLevel(tree1.root,5)
  print()
  print()
  print('level 2:', end= " ")
  tree2.printLevel(tree2.root,2)
  print()
  print('level 4:', end= " ")
  tree2.printLevel(tree2.root,4)
  print()
  print('level 6:', end= " ")
  tree2.printLevel(tree2.root,6)
  print()
  print()

  # print height and number of nodes of tree 1
  print(tree1.getHeight(tree1.root))
  print(tree1.numNodes())
  print()
  # print height and number of nodes of tree 2
  print(tree2.getHeight(tree2.root))
  print(tree2.numNodes())

main()
