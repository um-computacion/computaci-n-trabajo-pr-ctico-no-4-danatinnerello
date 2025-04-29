#funcion recursiva 

def fibonacci(n:int) -> int:
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("ingrese un numero"))
result = fibonacci(n)
print("su fibonacci es: ", result)