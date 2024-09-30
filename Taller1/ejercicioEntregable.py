articulos = []

while True:
    nombre_articulo = input("Ingrese el nombre del artículo (o 'salir' para finalizar): ")
    if nombre_articulo.lower() == 'salir':
        break
    precio_articulo = float(input("Ingrese el precio del artículo: "))
    cantidad_articulo = int(input("Ingrese la cantidad del artículo: "))
    articulos.append((nombre_articulo, precio_articulo, cantidad_articulo))

total_sin_descuento = sum(precio * cantidad for _, precio, cantidad in articulos)
total_articulos = sum(cantidad for _, _, cantidad in articulos)


def calcular_descuento(total_articulos, total_sin_descuento):
    if total_articulos >= 5:
        descuento = 0.20
    elif total_articulos >= 3:
        descuento = 0.10
    else:
        descuento = 0.0

    total_con_descuento = total_sin_descuento * (1 - descuento)
    return total_con_descuento, descuento


def determinar_metodo_pago(total_articulos):
    if total_articulos < 3:
        return "Efectivo"
    else:
        return "Tarjeta"


def aplicar_cargo_tarjeta(total, metodo_pago):
    if metodo_pago == "Tarjeta":
        return total * 1.02
    return total


total_con_descuento, descuento = calcular_descuento(total_articulos, total_sin_descuento)
metodo_pago = determinar_metodo_pago(total_articulos)
total_final = aplicar_cargo_tarjeta(total_con_descuento, metodo_pago)

print("\nResumen de la compra:")
print("-----------------------")
print(f"Número total de artículos: {total_articulos}")
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
print(f"Descuento aplicado: {descuento * 100:.0f}%")
print(f"Total después del descuento: ${total_con_descuento:.2f}")
print(f"Método de pago recomendado: {metodo_pago}")
print(f"Total final: ${total_final:.2f}")
