#funcion recursiva 

def fibonacci(n):
    try:
        # Intenta convertir la entrada a un entero
        n = int(n)
        
        # Verifica si el número es negativo
        if n < 0:
            return "Error: No se puede calcular Fibonacci para un número negativo"
        
        # Caso especial para fibonacci de 0
        if n == 0:
            return 0
        
        # Caso especial para fibonacci de 1
        if n == 1:
            return 1
        
        #caso feliz
        if n > 1:
            return fibonacci(n-1) + fibonacci(n-2)
        
    except ValueError:
        return "Error: Por favor ingresa un número entero válido"

def main():
    n = input("ingrese un numero")
    result = fibonacci(n)
    print(result)

if __name__ == "__main__":
    main()