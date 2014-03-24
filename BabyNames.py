## File: BabyNames.py
## Description: BabyNames:
##              It allows a user to query a data base of the most popular baby names
##              in the United States per decade for the past 11 decades
##              helper functions are created to provide structure to the program and reduce redundancy
##              The menu choices are: 
##               1 to search for names. 
##               2 to display data for one name. 
##               3 to display all names that appear in one decade. 
##               4 to display all names that appear in all decades. 
##               5 to display all names that are more popular in every decade. 
##               6 to display all names that are less popular in every decade. 
##               7(or any other input)to quit.
##              Used try-except-finally block to handle some inproper input and data reading from internet 
##              Total time consumed: 3 hours
## Author: Xiaoqin LI
## Date Created: 02/14/2014
## Date Last Modified:02/20/2014

import operator
import urllib.request

def create_dict():
    # read the database from the given url
    try:
        infile = urllib.request.urlopen("http://www.cs.utexas.edu/~mitra/csSpring2014/cs313/assgn/names.txt")
        name_dict = {}
        babyname_line = infile.readline()
        babyname_line = str(babyname_line, encoding = 'utf8')
        #read the data line by line and save them in a dictionary
        while babyname_line != "":        
            babyname_list = babyname_line.split()
            rank_list = []
            for i in range(1,len(babyname_list)):
                if int(babyname_list[i]) == 0:
                    rank_list.append(1001)
                else:
                    rank_list.append(int(babyname_list[i]))
            
            name_dict[(babyname_list[0])] = rank_list     
            babyname_line = infile.readline()
            babyname_line = str(babyname_line, encoding = 'utf8')   
        infile.close()
        return name_dict
    except urllib.error.HTTPError:
        print("The web link is not correct")
    except urllib.error.URLError:
        print("The internet may not be connected yet")
    finally:
        pass
    

# The menu choices to inquery database
def menu_choice():     
    print("Options:")
    print("Enter 1 to search for names.")
    print("Enter 2 to display data for one name.")
    print("Enter 3 to all names that appear in only one decade.")
    print("Enter 4 to all names that appear in all decades.")
    print("Enter 5 to all names that are more popular in every decade.")
    print("Enter 6 to all names that are less popular in every decade.")
    print("Enter 7 to quit.")
    print()
    b = input("Enter choice: ")
    return b

# search for names and display their highest rank through all decades
def ifNameExists(babyname):
    query_name = (input("Enter a name: ")).capitalize()
    if query_name in babyname:
        print()
        print("The matches with their highest ranking decade are:")
        highest_rank = min(babyname[query_name])
        count_highest_rank = babyname[query_name].count(highest_rank)
        if count_highest_rank == 1:
            print(query_name + ' ' + str(decades[babyname[query_name].index(highest_rank)]))
        # Print all years with highest ranking if there are ties.
        else:
            print(query_name, end = ' ')
            for i in range(len(babyname[query_name])):
                if babyname[query_name][i] == highest_rank:
                    print(str(decades[i]), end = ' ')
            print()
    else:
        print()
        print(query_name + " does not appear in any decade.")
    print()

# display all data for one name
def givenName_displayData(babyname):
    query_name = (input("Enter a name: ")).capitalize()
    if query_name in babyname:
        print()       
        print(query_name + ':', end = ' ')
        for entry in babyname[query_name]:
            print(entry, end = ' ')
        print()
        for i in range(0,len(babyname[query_name])):
            print(str(decades[i])+': '+ str(babyname[query_name][i]))
    else:
        print()
        print(query_name + " does not appear in any decade.")
    print()    

# display all names that appear in one decades.
def allNames_oneDecade(babyname):
    '''
    Used try-except-finally block to handle all possible inproper input caused errors.
    '''
    try:
        selected_decade = int(int(input("Enter decade: "))//10 * 10)  # make any integer valid in the given range 
    except ValueError:
        print("Could not query this because of an inproper input.")
    finally:
        pass
    try:
        decade_index = decades.index(selected_decade)
        selected_babynames = {}
        for key in babyname:
            if babyname[key][decade_index] < 1001:
                selected_babynames[key] = babyname[key][decade_index]
        # sort the list by mutiple levels of sorting: sort by rank first then by alphabet
        sorted_selected_babyname_list = sorted(selected_babynames.items(), key=operator.itemgetter(1,0))
        print("The names are in alphabetical: ")
        for entry in sorted_selected_babyname_list:
            print(format(entry[0],"12s") + str(entry[1]))        
    except ValueError:
        print("The decade you input was not recorded in the database.")
    except UnboundLocalError:
        print("The input decade should be an integer.")
    finally:      
        print()

# display all names that appear in all decades.       
def allNames_allDecade(babyname):
    selected_babynames = []
    name_counter = 0
    for key in babyname:
        if 1001 not in babyname[key]:
            selected_babynames.append(key)
            name_counter += 1
    print(str(name_counter) + " names appear in every decade. The names are: ")
    selected_babynames.sort() # sort the list by alphabet
    for entry in selected_babynames:
        print(entry)
    print()

# display all names that are more popular in every decade.
def allNames_morePopular(babyname):
    selected_babynames = []
    name_counter = 0
    for key in babyname:
        flag = True # set a flag to judge if the name is less popular in every decade
        for i in range(len(babyname[key])-1):
            if babyname[key][i] <= babyname[key][i+1]:
                flag = False
                break
        if flag == True:
            selected_babynames.append(key)
            name_counter += 1
    print(str(name_counter) + " names are more popular in every decade.")
    selected_babynames.sort() # sort the list by alphabet
    for entry in selected_babynames:
        print(entry)
    print()

# display all names that are less popular in every decade.
def allNames_lessPopular(babyname):
    selected_babynames = []
    name_counter = 0
    for key in babyname:
        flag = True 
        for i in range(len(babyname[key])-1):
            if babyname[key][i] >= babyname[key][i+1]:
                flag = False
                break
        if flag == True:
            selected_babynames.append(key)
            name_counter += 1
    print(str(name_counter) + " names are less popular in every decade.")
    selected_babynames.sort() # sort the list by alphabet
    for entry in selected_babynames:
        print(entry)
    print()
    
def main():
    # define decades tuple as a global variable to be used in other functions
    global decades
    decades = (1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000)
    
    babyname_dict = create_dict() #Create a dictionary to hold the baby names from the database.
    
    if babyname_dict != None:
        a = menu_choice()
        choice_list = ['1','2','3','4','5','6']
        '''
        create a while loop in which we display the menu choices. Read the user's choice
        and call a function to perform the necessary action. If the user chooses
        to quit, break out of the loop.
        '''
        while a in choice_list:
            if a == '1':
                ifNameExists(babyname_dict)
            elif a == '2':
                givenName_displayData(babyname_dict)
            elif a == '3':
                allNames_oneDecade(babyname_dict)
            elif a == '4':
                allNames_allDecade(babyname_dict)
            elif a == '5':
                allNames_morePopular(babyname_dict)
            elif a == '6':
                allNames_lessPopular(babyname_dict)          
            a = menu_choice()
    print()
    print()
    print("Goodbye")
    
main()
