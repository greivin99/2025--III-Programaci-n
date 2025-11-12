from Producto import Producto
from producto_repo import Producto_Repo

repo = Producto_Repo()

def store(data):
    nuevo = Producto(data[0], data[1], float(data[2]), data[3])
    repo.save(nuevo)

def get_all_products():
    return repo.find_all()

def find_by_name(name_seq):
    return repo.find_by_name(name_seq)

def find_by_price_range(min_price, max_price):
    return repo.find_by_price_range(min_price, max_price)

def update_product(product_id, nuevo_precio, nuevo_proveedor):
    repo.update(product_id, nuevo_precio, nuevo_proveedor)

def delete_product(product_id):
    repo.delete(product_id)
