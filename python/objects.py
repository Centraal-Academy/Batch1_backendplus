class User:
    '''Objeto user, recibe argumento name para inicializar'''
    def __init__(self, name):
        self.name = name
        self.__last_name = ''
        self._dateAdded = ''

    @property
    def date(self):
        print('soy un getter')
        return self._dateAdded

    @date.setter
    def date(self, value):
        raise NameError("El atributo es de solo lectura")

    def __log(self):
        print("se ejecuto algo")
        
    def give_me_last_name(self, value):
        '''funcion para poner apellido'''
        self.__last_name = value
        self.__log()
    
    def get_complete_name(self):
        return self.name + ' ' + self.__last_name

class Student(User):
    '''Clase para estudiantes, hereda de user, recibe argumentos de padre'''
    def __init__(self, name, program):
        User.__init__(self, name)
        self.program = program

    def __get_program(self):
        return self.program

    def __repr__(self):
        return self.get_complete_name() + ' ' + self.__get_program()
    
    def give_me_last_name(self, value, new_program):
        '''OVERRIDE : funcion para poner apellido y programa'''
        self.__last_name = value
        self.program = new_program
        