#import the employee_class so that we can make a subclass called ProductionWorker
import employee_class
# create a class called ProductionWorker with the attributes shift number and hourly pay.
class ProductionWorker(employee_class.Employee):
    def __init__(self, name, number, shift, pay):
        employee_class.Employee.__init__(self, name, number)
        self.__shift = shift
        self.__pay = pay

    # create the additional mutator methods for the subclass
    def set_shift(self, shift):
        self.__shift = shift

    def set_pay(self, pay):
        self.__pay = pay

    # create the accessor methods for the subclass
    # the accessor method should return either the day shift or night shift that the employee is working
    def get_shift(self):
        if self.__shift == 1:
            return "day shift (1)"
        else:
            return "night shift (2)"
    def get_pay(self):
        return self.__pay