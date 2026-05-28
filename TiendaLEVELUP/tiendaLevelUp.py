from pymongo import MongoClient

#establecer conexión con MongoDB
client = MongoClient('mongodb://localhost:27017/')

#seleccionar la base de datos y la colección
db = client['tienda_level_up']
coleccion = db['catalogo_productos']

#definir el documento como un  diccionario
consola = {
    "nombre": "PlayStation 5",
    "marca": "Sony",
    "precio": 499.99,
    "stock": 10,
    "especificaciones": {
        "procesador": "AMD Ryzen Zen 2",
        "memoria": "16 GB GDDR6",
        "color": "Blanco"
    }

}


#insertar el documento en la colección
resultado = coleccion.insert_one(consola)

#confirmar la operación
print(f"Producto insertado con ID: {resultado.inserted_id}")

