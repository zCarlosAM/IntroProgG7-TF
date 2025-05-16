# Ejercicio 2: Uso de computadoras en laboratorios
#------------------------------------------------------
# Autor: Carlos Daniel Aguirre Molina

# Descripción del ejercicio
#------------------------------------------------------
# Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras ocupadas y libres por laboratorio.

# Dependencias del programa
#------------------------------------------------------
import random   # Para el generador de números aleatorios
import os       # Para limpiar la pantalla

# Primero se definen algunas constantes para las cantidades de cada cosa
#------------------------------------------------------
COMPUTADORAS = 4
FILAS = 5
LABORATORIOS = 2

# Función para generar los laboratorios
#------------------------------------------------------
# Toma el parámetro "manual" en caso de que el usuario decida introducir manualmente los datos de la computadora
def crear_laboratorio(manual):
    # Se crea un array vacío del laboratorio que contendrá cada una de las 5 filas
    laboratorio = []
    
    # A continuación, se van creando las filas en base a la constante FILAS anteriormente definida
    for i in range(FILAS):
        if(manual):
            print("-" * 32)
            print(f"Fila {i+1}")
            print("-" * 32)
        fila = []
        
        # También se hace lo mismo para las computadoras
        for j in range(COMPUTADORAS):
            # Un valor Verdadero indicará que el equipo se encuentra ocupado y uno Falso indicará que el equipo se encuentra libre
           
            # En caso de que el usuario haya pedido introducir los valores manualmente, se le pide que los ingrese
            if(manual):
                computadora = bool(int(input(f"Ingrese un valor para la computadora {j+1}: ")))
            # En caso contrario, se generan aleatoriamente
            else:
                computadora = bool(random.randint(0,1))
            
            # Antes de terminar, se añade la computadora al array de la fila
            fila.append(computadora)
        # Y el array de la fila se añade al laboratorio
        laboratorio.append(fila)
    
    # Y finalmente, retornamos el array del laboratorio
    return laboratorio
 
# Función para mostrar el laboratorio
#------------------------------------------------------
def mostrar_laboratorio(laboratorio, num):
    # Primero se muestra el nombre del laboratorio que estamos observando, obviamente
    print(f"Laboratorio {num + 1}")
    print("-" * 32)
    
    # Luego definimos algunas variables para contabilizar las computadoras ocupadas y disponibles. Se volverán a usar más tarde.
    ocupadas = 0
    libres = 0
    
    # Usaremos un contador para enumerar las filas.
    contador = 1
    for fila in laboratorio:
        # Mostramos número de la fila
        print(f"{contador}:", end=" ")
        
        # Y representamos visualmente la disponibilidad de cada computadora.
        for computadora in fila:    
            if computadora:
                # Si el valor de la computadora es Verdadero, mostrar una X para indicar que se encuentra ocupada.
                print("X", end=" ")
                # No olvidarse de sumar un 1 al contador de computadoras ocupadas.
                ocupadas += 1
            else:
                # Si el valor es Falso, mostrar una O para indicar que se encuentra disponible .
                print("O", end=" ")
                # Sumamos un 1 a las computadoras libres.
                libres += 1
        # Añadimos una nueva línea y sumamos 1 al contador para luego repetir el mismo proceso con la siguiente fila.
        print("")
        contador += 1
    
    # Una vez hayamos terminado con todas las filas, mostrar la cantidad total de computadoras ocupadas y libres.
    print(f"\nOcupadas: {ocupadas}\nLibres: {libres}")
    print("-" * 32)    

# Función principal del programa
#------------------------------------------------------
def main():
    # Se muestra una pantalla para seleccionar el modo del programa
    os.system("cls || clear")
    print("Uso de computadoras en un laboratorio")
    print("-" * 32)
    print("1. Modo manual")
    print("2. Modo aleatorio")
    print("-" * 32)
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        manual = True
    elif opcion == 2:
        manual = False
    else:
        # En caso de que no se introduzca una opción válida, el programa finaliza
        print("Opción no válida")
        return
    
    # Creamos un array vacío de laboratorios
    laboratorios = []

    # Añadimos laboratorios al array según la cantidad especificada en la constante de laboratorios
    os.system("cls || clear")
    for i in range(LABORATORIOS):
        # Operaciones adicionales en caso de que el modo manual se encuentra activado
        if(manual):
            print("-" * 32)
            print(f"Laboratorio {i+1}")
            print("Ingrese 1 para computadoras ocupadas o 0 para disponibles")
            
        laboratorios.append(crear_laboratorio(manual))
        
        # Lo mismo que el comentario anterior
        if(manual):
            os.system("cls || clear")
            
    # Y por último mostramos cada laboratorio
    os.system("cls || clear")
    for i in range(LABORATORIOS):
        mostrar_laboratorio(laboratorios[i], i)

# Y como no podría faltar, la ejecución de la función main
#------------------------------------------------------
if __name__ == "__main__":
    main()