def fibonacci_NO_recursiva(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2 :
        return 1
    
    a,b = 0,1
    suma = a + b 

    for i in range(2, n):
        c = a + b 
        suma =suma + c 
        a,b = b,c
    return suma 


n = int(input("ingrese un numero"))
result = fibonacci_NO_recursiva(n)
print(result)