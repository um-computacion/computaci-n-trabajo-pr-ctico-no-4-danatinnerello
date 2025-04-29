class SoloListasError(Exception):
    ... 


def aplanar_lista(lista):
    #verifica si el elemento es una lista
    if not isinstance(lista, list):
            raise SoloListasError()
    resultado = []
    for elemento in lista:
        # si elelemento es una lista lo aplanamos recursivamente
        if isinstance(elemento, list) :# Si el elemento es una lista, aplicamos recursión
            resultado.extend(aplanar_lista(elemento))# Aplanamos la sublista y extendemos nuestro resultado
        elif isinstance(elemento, (int,float,str)) :# Si el elemento es una lista, aplicamos recursión
            resultado.append(elemento)# Aplanamos la sublista y extendemos nuestro resultado
        else:
            raise SoloListasError# Si es un elemento simple, lo agregamos directamente       
    return resultado

def main(): 
    try:
        entrada_usuario = input("Ingrese la estructura: ")
        # Usamos eval() para convertir la cadena a una estructura de datos real
        # ADVERTENCIA: eval() puede ser peligroso si se usa con entradas no confiables
        estructura = eval(entrada_usuario)
        if not isinstance(estructura, list):
            print("Error: La entrada debe ser una lista")
            return
            
        lista_plana = aplanar_lista(estructura)
        print(f"\nEstructura original: {estructura}")
        print(f"Estructura aplanada: {lista_plana}")
    except SoloListasError as e:
        print("Asegúrese de ingresar una estructura de datos Python válida")

if __name__ == "__main__":
    main()