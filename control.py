def main():
    dias = 3
    stands_por_dia = 4
    productos_por_stand = 3

 
    ventas_por_dia = []  
    total_general = 0

 
    for dia in range(1, dias + 1):
        ventas_dia = [] 
        total_dia = 0

        print(f"\n--- Día {dia} ---")
        for stand in range(1, stands_por_dia + 1):
            ventas_stand = []  
            total_stand = 0

            print(f"\nStand {stand}:")
            for producto in range(1, productos_por_stand + 1):
                venta = float(input(f"Ingrese venta del Producto {producto}: $"))
                ventas_stand.append(venta)
                total_stand += venta

            ventas_dia.append(ventas_stand)
            total_dia += total_stand


            print(f"\n-> Resumen Stand {stand}: Total = ${total_stand:.2f}")

        ventas_por_dia.append(ventas_dia)
        total_general += total_dia

        print(f"\n-> Resumen Día {dia}: Total = ${total_dia:.2f}")


    print("\n--- RESUMEN GENERAL ---")
    print(f"Total vendido en la feria: ${total_general:.2f}")

if __name__ == "__main__":
    main()