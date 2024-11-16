# Create a class called employee
class Employee:
    def __init__(self, name, ID, department, job):
        self.__name = name
        self.__id = ID
        self.__department = department
        self.__job = job
    # making mutator methods
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_department(self, dep):
        self.__department = dep

    def set_job(self, job):
        self.__job = job
    # making accessor methods
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__job

    def display_employee(self):
        print(f'{self.__name}, ID: {self.__id}, Department: {self.__department}, Job Title: {self.__job}.')
    # put this in a different location so that we can call it in other programs and create the instances of the class for the problem
