# Kristi Luu
# CIS 41A
class Country:
    '''
    A class called Country that will create objects when given rank, name, percent, and year.
    '''
    def __init__(self, rank, name, percent, year):
        '''Constructor for the Country class that takes in 4 arguments
        '''
        self._rank = rank
        self._name = name
        self._percent = percent
        self._year = year
    def print(self, *args):
        '''
        Function that will print the countries in a format
        '''
        print("{:40s} {:20s} {:10s}".format(self._name, self._percent, self._rank))
    def checkLetter(self, letter):
        '''
        Function that will return True if the country's first letter matches the 
        letter taken in by the function, and False otherwise
        '''
        return self._name[0] == letter
    def __lt__(self,rhs):
        return self._name < rhs._name