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
    return value1 + value2

def compareValue(value):
    if value < 5:
        raise ValueError("el valor es menor")
    return True
