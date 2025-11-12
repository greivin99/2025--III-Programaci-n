import io_utils
import product_manager

def process(option):
    if option == 1:
        data = read_product_data()
        product_manager.store(data)
    elif option == 2:
        print_products(product_manager.get_all_products())
    elif option == 3:
        search_submenu()
    elif option == 4:
        modify_product()
    elif option == 5:
        delete_product()
    elif option == 6:
        print("Saliendo...")
        exit()
    else:
        print("Opcion invalida.")

def read_product_data():
    print("\n--- Ingresar de datos del producto ---")
    nombre = io_utils.read_str("Nombre del producto: ")
    categoria = io_utils.read_str("Categoria: ")
    precio = io_utils.read_str("Precio: ")
    proveedor = io_utils.read_str("Nombre del proveedor: ")
    return [nombre, categoria, precio, proveedor]

def print_products(lista):
    for p in lista:
        print(p)

def search_submenu():
    print("\n--- Buscar productos ---")
    print("a) Por nombre")
    print("b) Por rango de precios")
    op = io_utils.read_str("Seleccione opcion: ").lower()
    if op == "a":
        name = io_utils.read_str("Fragmento del nombre: ")
        print_products(product_manager.find_by_name(name))
    elif op == "b":
        min_p = float(io_utils.read_str("Precio minimo: "))
        max_p = float(io_utils.read_str("Precio máximo: "))
        print_products(product_manager.find_by_price_range(min_p, max_p))
    else:
        print("Opción invalida.")

def modify_product():
    pid = int(io_utils.read_str("ID del producto a modificar: "))
    new_price = float(io_utils.read_str("Nuevo precio: "))
    new_supplier = io_utils.read_str("Nuevo proveedor: ")
    product_manager.update_product(pid, new_price, new_supplier)
    print("Producto actualizado.")

def delete_product():
    pid = int(io_utils.read_str("ID del producto a borrar: "))
    product_manager.delete_product(pid)
    print("Producto eliminado.")
