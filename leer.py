import csv

print("=" * 30)
print("Resumen de ventas")
print("=" * 30)

with open("ventas.csv", encoding="utf-8", newline="") as archivo:
    
    lector = csv.reader(archivo)
    cabecera = next(lector)
    total_venta = 0

    for fila in lector:
        producto = fila[0]
        cantidad = int(fila[1])
        precio = float(fila[2])

        subtotal = cantidad * precio
        total_venta += subtotal
        print(f"Producto: {producto} | Cantidad: {cantidad} | Precio: ${precio} | Subtotal: ${subtotal}")
    print("=" * 30)
    print(f"TOTAL: ${total_venta}")
