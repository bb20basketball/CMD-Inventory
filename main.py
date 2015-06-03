###First I will just do a command based example#
"""
This program finds the inventory of an item and allows 
you to manage it
"""
import json
import sys

##The program is working very nicely and I am liking
#all the functions because that makes updating and just coding##
##in general much easier!##
class Master:
    """
    The class I am putting it in is called Master
    """
    def __init__(self):
        """
        Just sets some variables and starts the controller function
        """
        self.controller()
        self.what_item, self.keyword, self.items = 0
        self.new_amount, self.keywords, self.file = 0

    def controller(self):
        """
        The controller function is the home screen of the program. Decides where to go
        """
        what_do_you_want = raw_input("(C)heck or (M)anage Inventory? ")
        self.updater() 
        if what_do_you_want.lower() == 'm':
            self.changer()
        elif what_do_you_want.lower() == 'c':
            self.checker()


    def enter_in_item(self):
        """
        The enter_in_item function just grabs the item and sees if it is in keyword
        or id format
        """
        self.what_item = raw_input("Enter in ID or keyword... ")
        if self.what_item in self.items:
            self.for_id(self.what_item)
        elif self.what_item in self.keywords:
            self.keyword = self.what_item
        else:
            print "Invalid Item"
            sys.exit()

    def checker(self):
        """
        The checker function checks the inventory
        """
        self.enter_in_item()
        self.updater()
        print "Avaible SOH = " + str(self.files[self.keyword]['quantity'])
        self.controller()

    def changer(self):
        self.enter_in_item()
        self.new_amount = raw_input("Enter in the new inventory number or subtract/add with operators... ")
        self.writer(self.new_amount)
    
    def writer(self, amount):
        self.updater()
        new_total = amount[1:]
        if amount[0] == '+': #making adding and subtracting separate for now#
            amount = int(self.files[self.keyword]['quantity'])+int(new_total)
        elif amount[0] == '-':
            amount = int(self.files[self.keyword]['quantity'])-int(new_total)
        else:
            pass

        print "New inventory is " + str(amount)
        self.files[self.keyword].update({"quantity":amount})    
        self.dumper(self.files)
        self.updater()
        self.controller()

    def dumper(self, dumping):
        json.dump(dumping, open(your_file_location_here, "w"))

    def updater(self):
        with open(your_file_location_here) as fp:
            self.file = json.load(fp)
        self.items = []
        self.keywords = []
        for i in self.files:
            self.items.append(self.files[i]["id"])
            self.keywords.append(i)

    def for_id(self, number):
        for i in self.files:
            if self.files[i]["id"] == number:
                self.keyword = i
    
if __name__ == "__main__":
    Master()
