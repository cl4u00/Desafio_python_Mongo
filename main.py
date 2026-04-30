# Definir el documento como un diccionario
consola = {
    "nombre": "Nintendo Switch OLED",
    "marca": "Nintendo",
    "precio": 350000,
    "stock": 10,
    "especificaciones": {
        "pantalla": "OLED 7 pulgadas",
        "color": "Neon"
    }
}

# Ejecutar la inserción
resultado = coleccion.insert_one(consola)

# Confirmar la operación
print(f"Producto insertado con ID: {resultado.inserted_id}")