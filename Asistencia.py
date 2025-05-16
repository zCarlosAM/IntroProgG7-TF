# Registro de asistencia académica por sección en la UAM
# Cada sección tiene 6 estudiantes
# Se registran 5 días de clases

secciones = ['A', 'B', 'C']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

total_general = 0

for seccion in secciones:
    print(f"Sección {seccion}")
    total_seccion = 0
    
    for estudiante in range(1, 7):
        print(f"Estudiante #{estudiante}")
        asistencias_estudiante = 0
        
        for dia in dias:
            while True:
                respuesta = input(f"¿Estuvo presente el día {dia}? (S/N): ").strip().upper()
                if respuesta in ['S', 'N']:
                    break
                else:
                    print("Entrada inválida. Por favor ingrese 'S' o 'N'.")
            
            if respuesta == 'S':
                asistencias_estudiante += 1
        
        print(f"Total asistencias del Estudiante #{estudiante}: {asistencias_estudiante}")
        total_seccion += asistencias_estudiante
    
    print(f" Total asistencias en Sección {seccion}: {total_seccion}")
    total_general += total_seccion

print(f"Total general de asistencias en la semana: {total_general}")
 