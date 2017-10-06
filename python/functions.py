import my_exceptions as exc

def add_by(value1, value2):
    '''product of two values'''
    try:
        result = int(value1 * value2)
        return result
    except:
        print("el valor no es esperado")
        raise TypeError("hubo un pedo aca")

def sum_by(value1, value2):
    '''product of two values'''
    if value1 == 1:
        raise exc.AnotherError("El valor introducido por el usuario en value1 fue 1","ya cache un error personalizado")
    return value1 + value2

def compareValue(value):
    if value < 5:
        raise ValueError("el valor es menor")
    return True
