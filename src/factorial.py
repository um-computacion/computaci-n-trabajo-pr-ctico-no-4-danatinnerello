#funcion factorial NO recursiva


# def factorial_NO_recursiva(n:int)->int:
#     total = 1
#     while n > 0:
#         total = total * n
#         n = n - 1 
#     return total 

#funcion factorial recursiva


def factorial_recursiva(n):
    
    try:
        # Intenta convertir la entrada a un entero
        n = int(n)
        
        # Verifica si el número es negativo
        if n < 0:
            return "Error: No se puede calcular el factorial de un número negativo"
        
        # Caso especial para el factorial de 0
        if n == 0:
            return 1
        #caso feliz
        if n ==1 or n ==0:
            return 1 
        else:
            return n* factorial_recursiva(n-1)
        
    except (ValueError, TypeError):
           return "Error: Por favor ingresa un número válido"


def main():   
    n = input("ingrese un numero")
    result = factorial_recursiva(n)
    print(result)
    
if __name__ == "__main__":
    main()