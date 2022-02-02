# Esta funcion nos sirve como parametro para ordenar por la cantidad de cada producto
def myKey(e):
    return e[2]


# Esta funcion nos sirve para resolver la primer consigna, solo basta con especificar los tamaños por este caso solo son dos
def primer_consigna(productos,lista2,tamaño,palabra):
    productos_maximos = []
     
    for producto in productos:
        cantidad = 0
        for elemento in lista2:
            # Buscamos que el producto que se esta iterando este en la otra lista y si lo encontramos
            # sumamos en 1 nuestra variable cantidad, estamos contabilizando cuantas veces aparece el producto
            # en la lista2 
            if producto[0] == elemento[1]:
                cantidad += 1
        # Agregamos una lista en nuestra lista, los datos que ocupamos son el id_product, name y la cantidad de ese producto
        # que aparece en la lista2
        productos_maximos.append([producto[0],producto[1],cantidad])
    
    # Aqui lo que hacemos es acomodar nuestra lista por medio de la cantidad de manera
    # descendente
    productos_maximos.sort(reverse=True,key=myKey)
    
    # Tenemos que imprimir los datos que nos piden en la consigna
    productos_impresion = productos_maximos[0:tamaño]
    productos_impresion_menores = productos_maximos[len(productos_maximos)-(tamaño+1):len(productos_maximos)-1]
    # imprimimos los n=tamaño productos
    print(f'\n\nLos {tamaño} productos mas {palabra} son los siguientes:')
    for producto in productos_impresion:
        print(f'Producto: {producto[1]} con {producto[2]} ventas')
        
    # imprimimos los n=tamaño productos
    print(f'\n\nLos {tamaño} productos menos {palabra} son los siguientes:')
    for producto in productos_impresion_menores:
        print(f'Producto: {producto[1]} con {producto[2]} ventas')