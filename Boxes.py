## File: Boxes.py
## Description: Boxes: Nesting Boxes.Get and store all nested
##              boxes combinations by recursion.Recursion algorithm are simplied by
##              a constaint: the recursion will stop on those brach which currently
##              is no longer nested.               
##              Total time consumed: 100 minutes
## Author: Xiaoqin LI
## Date Created: 02/22/2014
## Date Last Modified:02/27/2014

# create a list to store all nested subset.
nested_boxes_list = []

def creating_boxes_list():
    '''
    * Create an empty list of boxes
    * Open and read the file boxes.txt
    * Read each line of input, store in a list and sort 
      and add to list of boxes
    * Sort the list of boxes by key = lambda column: (column[2],column[1],column[0]) and return the whole list
    '''
    boxes_data_list = [] 
    infile = open("boxes.txt","r")
    num_boxes = int(infile.readline())   
    for i in range(0, num_boxes):
        box_data_int = []
        box_data = (infile.readline()).split()
        for entry in box_data:
            box_data_int.append(int(entry))
        box_data_int.sort()
        boxes_data_list.append(box_data_int)
    sorted_boxes_data_list = boxes_data_list.sort(key = lambda column: (column[2],column[1],column[0]))
    infile.close()
    return boxes_data_list

def getAllSubsets(a, b, lo):
    '''
    Get and store all nested boxes combinations by recursion.
    Recursion algorithm are simplied.
    '''
    hi = len(a)
    if (lo == hi):
        # store nested boxes combinations in a global list
        nested_boxes_list.append(b) 
        return
    else:
        c = b[:]
        b.append(a[lo])
        getAllSubsets(a, c, lo + 1)
        if len(b) > 1:
            # recursion algorithm simplied by this constraint: only do recursion on those lists having nested boxes
            if b[len(b)-1][0] > b[len(b)-2][0] and b[len(b)-1][1] > b[len(b)-2][1] and b[len(b)-1][2] > b[len(b)-2][2]:
                getAllSubsets(a, b, lo + 1)
        else:
            getAllSubsets(a, b, lo + 1)
        
def main():
    # Get all boxes in a list
    boxes_list = creating_boxes_list() 
    subset_boxes = []
    
    # Get all nested boxes combinations
    getAllSubsets (boxes_list, subset_boxes, 0)
    
    # Go through all sets of nesting boxes and find ones with maximum length
    max_nest_length = 1
    for entry in nested_boxes_list:
        if len(entry) > max_nest_length:
            max_nest_length = len(entry)
        
    # Print largest set of nesting boxes
    if max_nest_length >= 2:
        print("Largest Subset of Nesting Boxes")
        for entry in nested_boxes_list:
            if len(entry) == max_nest_length:
                for box in entry:
                    print(box)
                print()
    else:
        print("No Nesting Boxes")
    
main()

