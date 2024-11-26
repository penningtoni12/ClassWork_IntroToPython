# make a class called employee with name and number attributes
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    #create mutator methods
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number
    # create the accessor methods
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number