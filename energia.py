
consumo_edificios = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0
}


turnos = ['mañana', 'tarde', 'noche']


for edificio in consumo_edificios:
    print(f"\nRegistro para edificio {edificio}:")
    # 7 días
    for dia in range(1, 8):
        print(f" Día {dia}:")
        # 3 turnos
        for turno in turnos:
            while True:
                try:
                    consumo = float(input(f"  Ingrese kWh consumidos en el turno {turno}: "))
                    consumo_edificios[edificio] += consumo
                    break
                except ValueError:
                    print("  Entrada inválida. Use un número válido.")

print("\n--- Reporte de Consumo Energético ---")
for edificio, total in consumo_edificios.items():
    promedio = total / 7
    print(f"Edificio {edificio}: Total = {total:.2f} kWh, Promedio diario = {promedio:.2f} kWh")
