#funcion factorial NO recursiva


def factorial_NO_recursiva(n:int)->int:
    total = 1
    while n > 0:
        total = total * n
        n = n - 1 
    return total 

n = int(input("ingrese un numero"))
result = factorial_NO_recursiva(n)
print("el factorial es: ",result)

