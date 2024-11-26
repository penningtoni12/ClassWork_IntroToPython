# import the employee class that was coded in programming exercise 1
import employee_class
# create a suclass of Employee that has the attributes annual salary and annual bonus
# we have to use the Employee class in the ShiftSupervisor class so it can be inherited.
# first, we have to use the module employee_class to use the Employee class
class ShiftSupervisor(employee_class.Employee):
    def __init__(self, name, number, annual_salary, annual_bonus):
        # call the init from the Employee class so that we may use it's attributes in the subclass
        employee_class.Employee.__init__(self, name, number)
        # create the private salary and bonus attributes
        self.__salary = annual_salary
        self.__bonus = annual_bonus
    # create mutator methods for the ShiftSupervisor class * remember to use self as a condition for the method's defining
    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    # create the accessor methods for the ShiftSupervisor class, remember to use self as the condition
    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus