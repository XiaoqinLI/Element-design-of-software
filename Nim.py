# File: Nim.py
# Description: learned the beauty of binary.
#              In the code, two functions are called in Main(). The results satisfies the requirement.
# Author: Xiaoqin LI
# Date Created: 01/15/2014
# Date Last Modified:01/17/2014

def main():
    infile = open("nim.txt","r")                     # open the data file
    num_games = int(infile.readline())               # read in the first line of data file to get the number of nim games.

    for i in range(0,num_games):                     # create a loop to go through each game
        gamedata = infile.readline()                 # Read a line which conctains heaps of counters for current game,
        gamedata = gamedata.split()                  # Split the line to get number of counters in each pile
        num_heaps = len(gamedata)
        counters_list = []
        for entry in gamedata:                       # Convert the number of counters into integers and save them in a list
            counters_list.append(int(entry))
            
        nim_sum = find_nim_sum(counters_list)        # call find_nim_sum function to calculate  sum of Nim.
        if nim_sum == 0:                             # Lose Game and continue to next game 
            print("Lose Game")
            continue
        else:                                        # Find first step to win the game
            counters_number, heap_number = first_output(nim_sum, counters_list) #
            if counters_number > 1:
                print("Remove "+ str(counters_number)+" counters from Heap " + str(heap_number))
            else:
                 print("Remove "+ str(counters_number)+" counter from Heap " + str(heap_number))
            
    infile.close()                                   # all games have been played, close the game file.
     
def find_nim_sum(counters_ingame):                   # calculating and return the sum of nim
    result = 0
    for entry in counters_ingame:
        result = result^entry
    return result

def first_output(nim, counters_ingame):              # Compute individual nim sum with each pile and return the number
                                                     # of pile and its counters that will be removed
    for entry in counters_ingame:
        individual_sum = nim^entry
        if individual_sum < entry:                   # If nim sum is less than the number of counters in
                                                     # that pile remove the difference 
            difference = entry - individual_sum
            heap_num = counters_ingame.index(entry) + 1
            return difference, heap_num
        
main()






