import shelve, os

#Variable used to name the shelf file which will be created
shelve_name = 'new_shelf.shlv'



"""
Optional parameters for opening the shelf file are:
    'r' ->  Open existing database for reading only
    'w' ->  Open existing database for reading and writing
    'c' ->  Open database for reading and writing, creating it if it doesn't exist
            ('c' is the default value, can verify by deleting insert_pickle's
            argument)
    'n' ->  Always create a new, empty database, open for reading and writing
"""

#Requests a key value and value parameter from user, opens or verified existence
#of shelf file, adds values as dictionary key/value pair, closes shelf
def insert_pickle():
    user_input1 = str(input("Please enter the key value: ").title())
    user_input2 = str(input("Please enter the value parameter: ").title())
    my_shelve = shelve.open(shelve_name, flag= 'c')
    my_shelve[user_input1] = user_input2
    my_shelve.close()

#Asks user if adding new pickle is desired, if 'Y' entered will ask infinitely
#and add key/value pairs as appropriate
def insert_another():
    user_input3 = str(input("Add another pickle? ").title())
    if user_input3 == 'Y':
        insert_pickle()
        insert_another()
    else:
        pass

#Upon entering any value other than 'Y' in insert_another(), asks a single time
#which key user would like to access, prints associated value
def print_a_pickle():
    user_input4 = str(input("Which key would you like to access? ").title())
    print(new_shelve[user_input4])

insert_pickle()
insert_another()

#The shelf is created within the insert_pickle() function, is closed by the function
#and needs to be reopened
new_shelve = shelve.open(shelve_name)

#Regardless of the final number of key/value pairs, any key can be accessed and its
#associated value printed
print_a_pickle()

#If the line below is commented out, the shelf file can be verified to exist
#in the project folder (and would need to be manually deleted)
os.remove(shelve_name)