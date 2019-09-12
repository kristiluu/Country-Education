# Kristi Luu
# CIS 41A
# The data structure that I chose to use is a list. The list is especially useful because 
# when doing the check for the ranking display, I can traverse the list by index and 
# more easily use the any() function to check for the first letter in the list of objects.
# The elements of the list are the Country objects (thus, in this project, 179 Country objects in a list)
# They are in the order that they are read in through the text file. 
# The list is best option of the data structures because I could use list-comprehension to 
# read in the data, as well as use it with the any() function when checking the letter 
# and country name. The list allows less usage of a loop.
import files
import csv
import re
from country import Country

class userInterface: 
    '''This is the userInterface class'''
    def __init__(self):
        '''Constructor for the userInterface class. It will make the CSV file, read in the
        file, and create a list of all the countries from the file.
        It will also print the number of objects created/read in. 
        '''
        self._csvname = files.toCSV.toCSV()
        self._menu = {'r': self.displayRank, 'n': self.displayName, 'q': quit}
        with open(self._csvname) as infile :
            reader = csv.reader(infile)
            self._database = [Country(line[0], line[1], line[2], line[3]) for line in reader] #comprehension
            print ("Read in:", len(self._database), "countries")
        self.run()
        
    def run(self):
        '''
        Function that will display the options/menu and allow user to enter their choice.
        '''
        print('\nn. Countries by name\nr. Countries by ranking\nq. Quit')
        user = input("Your choice: ").lower()
        if len(user) != 1 or user not in 'rnq':
            print('\nn. Countries by name\nr. Countries by ranking\nq. Quit')
            user = input("Your choice: ")
        else: 
            self._menu[user]()
            self.run()

    def displayRank(self):
        '''
        Function that will prompt the user to enter 2 integers between 1 and 179. There will be 
        checks that occur such as checking for the number of integers entered (should only be 2)
        and the order it's written in, etc.
        
        If everything is entered correctly, the program will display the ranking of the countries based
        on the 2 integers entered by the user.
        '''
        correctInput = True
        while correctInput:
            try: 
                rankNumChoice = input("Enter min and max ranking: ")
                numList = re.findall('\d+[.]\d+|(\d+)', rankNumChoice)
                if not len(numList) == 2:
                    raise ValueError("Enter 2 integers please")
                if not(numList[0]) or not(numList[1]): #an empty element/string = false
                    raise TypeError("Enter 2 integers please")
                if not int(numList[0]) < int(numList[1]):
                    raise ValueError("min and max must be between 1 and 179 and min < max")
                if int(numList[0]) < 1 or int(numList[1]) > 179:
                    raise ValueError("min and max must be between 1 and 179 and min < max")
                else:
                    correctInput = False
            except ValueError as e:
                print(str(e))
                self.run()
            except TypeError as e:
                print(str(e))
                self.run()
        print ("{:40s} {:20s} {:10s}".format("Name", "% GPD", "Rank"))
        for i in range(int(numList[0])-1, int(numList[1])):
            self._database[i].print()

    def displayName(self):
        '''
        Function that displays the countries by name. The order is based on the letter that the 
        user chooses. It will prompt the user for the letter, check if a country starting with that
        letter exists, then displays it in a proper format.
        '''
        countryLetter = input("Enter first letter of country name: ").upper()
        if len(countryLetter) != 1 or not countryLetter.isalpha():
            countryLetter = input("Enter first letter of country name: ").upper()
        else:
            if not any(object.checkLetter(countryLetter) for object in self._database):
                print("A country with that letter does not exist. Please try again")
            else: 
                print ("{:40s} {:20s} {:10s}".format("Name", "% GPD", "Rank"))
                for object in sorted(self._database):
                    if object.checkLetter(countryLetter):
                        object.print()
                        
def main(): 
    ui = userInterface()
main()