
def recursiva(number, times):
    print(f"factor a : {number}")
    if number < times :
        recursiva(number + 1, times)

def factorial(n):
    if n == 1:
        return 1
    else:
        import pdb; pdb.set_trace()
        return n * factorial(n-1)

if __name__ == '__main__':
    recursiva(2, 10)
    factorial(10)
