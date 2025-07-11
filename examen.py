"https://github.com"

productos = {'8475HD': ['hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['hp', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
opcion = 0 


def stock_marca():
    disponible = input("ingrese la marca que desea buscar: ").lower()
    for i in productos.values():
        for i in stock:
        if disponible.lower() in i:
            print (f"stock la marca {disponible}:{i}")
            
def busqueda_precio():
    try:
        buscar = input("ingrese el precio maximo")
        buscar2 = input("ingrese precio minimo")
    except ValueError:
        print ("debe ingresar un valor numerico")
        return
    if buscar and buscar2 in stock.values:
        print ("a")
def eliminar_producto():
    eliminar = input("ingrese el modelo a eliminar: ").lower()
    if eliminar in productos.values():
        del productos[eliminar]
        del stock[eliminar]
        print ("producto eliminado")

     

while opcion !=5:

    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Eliminar producto.")
    print("4. Salir")

    try:
        opcion = int(input("ingrese una opcion"))
    except ValueError:
        print ("debe ingresar un valor numerico")
        continue
    if opcion == 1:
        stock_marca()
    elif opcion == 2:
        busqueda_precio()
    elif opcion == 3:
        eliminar_producto()
    elif opcion == 4:
        print ("Programa finalizado")