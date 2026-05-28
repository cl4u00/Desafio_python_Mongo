def insertar_producto():
    nombre = input("Nombre: ")
    marca = input("Marca: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    
    producto = {"nombre": nombre, "marca": marca, "precio": precio, "stock": stock}
    
    if input("¿Es Consola? (S/N): ").strip().upper() == 'S':
        producto["especificaciones"] = {
            "almacenamiento": input("Almacenamiento: "),
            "color": input("Color: ")
        }
        
    coleccion.insert_one(producto)
    print("Producto registrado.")

def actualizar_stock():
    nombre = input("Producto a actualizar: ")
    if coleccion.find_one({"nombre": nombre}):
        inc = int(input("Cantidad a sumar: "))
        coleccion.update_one({"nombre": nombre}, {"$inc": {"stock": inc}})
        print("Stock actualizado.")
    else:
        print("No encontrado.")

def eliminar_producto():
    nombre = input("Producto a eliminar: ")
    producto = coleccion.find_one({"nombre": nombre})
    if producto:
        print(producto)
        if input("¿Seguro que desea eliminar? (S/N): ").strip().upper() == 'S':
            coleccion.delete_one({"nombre": nombre})
            print("Eliminado.")
    else:
        print("No encontrado.")