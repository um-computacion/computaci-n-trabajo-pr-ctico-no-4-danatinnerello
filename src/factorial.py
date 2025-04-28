#funcion factorial NO recursiva


# def factorial_NO_recursiva(n:int)->int:
#     total = 1
#     while n > 0:
#         total = total * n
#         n = n - 1 
#     return total 

#funcion factorial recursiva

def factorial_recursiva(n:int):
    if n ==1 or n ==0:
        return 1 
    else:
        return n* factorial_recursiva(n-1)
    

n = int(input("ingrese un numero"))
result = factorial_recursiva(n)
print("el factorial es: ",result)


