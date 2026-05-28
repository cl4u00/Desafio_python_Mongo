from pymongo import MongoClient

#establecer conexión con MongoDB
client = MongoClient('mongodb://localhost:27017/')

#seleccionar la base de datos y la colección
db = client['tienda_level_up']
coleccion = db['catalogo_productos']

#definir el documento como un diccionario

consola = [
    {
    "nombre": "xbox series x",
    "marca": "Microsoft",
    "precio": 499.99,
    "stock": 10,
    "especificaciones": {
        "procesador": "AMD Ryzen Zen 2",
        "memoria": "16 GB GDDR6",
        "color": "Blanco"
        }          
    },
    {
    "nombre": "Nintendo Switch",
    "marca": "Nintendo",
    "precio": 299.99,
    "stock": 15,
    "especificaciones": {
        "procesador": "NVIDIA Custom Tegra",
        "memoria": "4 GB LPDDR4",
        "color": "Neón rojo y azul"
    }       
    }]      

#insertar el documento en la colección
resultado = coleccion.insert_many(consola)

#confirmar la operación
print(f"Productos insertados con IDs: {resultado.inserted_ids}")