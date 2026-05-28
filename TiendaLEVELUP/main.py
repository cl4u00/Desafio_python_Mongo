from tiendaLevelUp import insertar_producto, actualizar_stock, eliminar_producto
from catalogo import consultar_catalogo

def mostrar_menu():
    print("\n=== LEVEL UP ===")
    print("1. Insertar")
    print("2. Consultar")
    print("3. Actualizar Stock")
    print("4. Eliminar")
    print("5. Salir")

    while True:
        mostrar_menu()
        opc = input("Seleccione: ")
        
        if opc == "1": insertar_producto()
        elif opc == "2": consultar_catalogo()
        elif opc == "3": actualizar_stock()
        elif opc == "4": eliminar_producto()
        elif opc == "5": break
        else: print("Inválido.")

