class User:
    '''Clase Usuario. Parametros:
    name : nombre del usuario'''
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Student(User):
    '''Student inherits from User \n
    Arguments : name for superclass and \n
    program for student program'''

    __logging = ''

    def __init__(self, name, program):
        User.__init__(self, name)
        self.program = program
        self._date = "sep 26"

    @property
    def date(self):
        print("get method")
        return self._date

    @date.setter
    def date(self, value):
        print("set method")
        raise NameError("date is an only-read property")

    def __log(self, log_info):
        self.__logging = log_info
        print(self.__logging)

    def get_complete_name(self):
        '''get user complete name'''
        self.__log("return complete name")
        return self.get_name() + self.program

    def __repr__(self):
        return repr(self.name + ' ' + self.program)

class Counter:
    '''counter class'''
    count = 0

    def __init__(self):
        self.__class__.count += 1
