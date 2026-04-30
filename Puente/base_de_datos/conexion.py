from pymongo import MongoClient

# Establecer conexión con el servidor local
cliente = MongoClient('mongodb://localhost:27017/')

# Seleccionar la base de datos y la colección
db = cliente['Tienda_LevelUp']
coleccion = db['catalogo_productos']


