## File: MagicSquare.py
## Description: Magic Square.The purpose of
##              this assignment is two-fold - generate odd dimension magic squares
##              using the above algorithm and generating all possible magic squares
##              for a given dimension using brute force (in this case through permutation).                        
##              Total time consumed: 90 minutes.
## Author: Xiaoqin LI
## Date Created: 03/08/2014
## Date Last Modified:03/16/2014


def makeSquare(n):
    '''
    Populate a 2-D n by n list with all 0 element
    create a magic square based on the numbers from 1 to n square
    '''
    # create a 2-D list with 0 element
    m_square = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        m_square.append(row)

    
    for i in range(1,n**2+1):
        # Place a 1 in the middle of the bottom row. 
        if i == 1:
            m_square[n-1][int((n-1)/2)]= 1
            row_index = n-1
            col_index = int((n-1)/2)
        
        # After k has been placed in the (i, j) square, place k+1 into the
        # square to the right and down, wrapping around the borders.
        # However, if the square to the right and down has already been filled,
        # or if you are in the lower right corner, then you must move to the square
        # straight up (from the last square that you were on) instead          
        else:
            if row_index == n-1 and col_index == n-1:
                row_index -= 1
                m_square[row_index][col_index] = i
            else:
                row_index += 1
                if row_index >= n:
                    row_index -= n
                col_index += 1
                if col_index >= n:
                    col_index -= n
                if m_square[row_index][col_index] == 0:
                    m_square[row_index][col_index] = i
                else:
                    row_index -= 1
                    if row_index < 0:
                        row_index += n
                    col_index -= 1
                    if col_index < 0:
                        col_index += n
                    row_index -= 1
                    m_square[row_index][col_index] = i
    return m_square

# Print the magic square in a neat format where the numbers
# are right justified, numbers are seperated by whitespace each line   
def printSquare(square):           
    for row in square:
        for value in row:
            print(format(value, '2d'), end = " ")
        print()
        
# Check if a list is a magic square
def checkSquare ( magicSquare ):
    # create a 3x3 2-D list based on the 1-D list
    magicSquare_2D = []
    counter = 0
    for i in range(3):
        row = []
        for col in range(3):
            row.append(magicSquare[counter])
            counter += 1
        magicSquare_2D.append(row)
        
    # Check if this 2-D list is a magic square
    flag_square = True    
    for column in range(3):
        total = 0
        for row in range(3):
            total += magicSquare_2D[row][column]
        if total != 15:
            flag_square = False
    for row in range(3):
        if sum(magicSquare_2D[row])!= 15:
            flag_square = False
    if magicSquare_2D[0][0] +  magicSquare_2D[1][1] +  magicSquare_2D[2][2] != 15:
        flag_square = False
    if magicSquare_2D[2][0] +  magicSquare_2D[1][1] +  magicSquare_2D[0][2] != 15:
        flag_square = False

    return flag_square            
    
# Generate all 3x3 magic squares
def permute (a, lo):
    hi = len(a)
    if (lo == hi):
        if checkSquare(a):
            printAllSquare(a)  
    else:
        for i in range (lo, hi):
            a[lo], a[i] = a[i], a[lo]     
            permute (a, lo + 1)
            a[lo], a[i] = a[i], a[lo]
            
# print out all 3x3 magic squares in a neat format
def printAllSquare(square_list):
    counter = 0
    for i in range(3):
        for j in range(3):
            print(format(square_list[counter], '2d'), end = " ")
            counter += 1
        print()
    print()
        
def main():
    
    # Prompt the user to enter an odd number 3 or greater
    # Check the user input. If it is not, prompt the user to re-enter
    # the number and check again and again.
    square_order = input("Please enter an odd number: ")
    while (not square_order.isdigit()) or (int(square_order)%2 != 1) or(int(square_order) < 3):
        print("Invalid input, please re-enter again: ")
        square_order = input("Please enter an odd number: ")
    print()
    square_order = int(square_order)
    
    # Create the magic square based on the order
    magic_square = makeSquare(square_order)
    
    # Print the magic square
    print("Here is a", square_order, "x", square_order, "magic square:")
    print()
    printSquare(magic_square)
    print()

    # Print all 3x3 magic squares
    print("All 3x3 magic square: ")
    print()
    # using brute force (through permutation) to find all 3X3 magic square.
    square_3_list = [1,2,3,4,5,6,7,8,9]
    permute (square_3_list, 0)
    
main()

