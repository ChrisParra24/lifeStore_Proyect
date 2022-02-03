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

# Funcion que limpia la lista
def limpia_lista(lista,index,tamaño):
    lista_limpia = []
    for elemento in lista:
        if elemento[2] != 0:
            lista_limpia.append(elemento)
    return lista_limpia

# Funcion que nos regresa los años
def regresa_años(ventas):
    años = []
    for venta in ventas:
        #obtenemos la fecha completa
        fecha = venta[3]
        año = fecha[6:len(fecha)]
        año = int(año)
        if len(años) == 0:
            años.append(año)
        else:
            if año not in años:
                años.append(año)
    return años

# Funcion que nos regresa el año y se le pasa una cadena    
def extrae_año(fecha):
    año = fecha[6:len(fecha)]
    return int(año)

# Funcion que nos regresa el mes y se le pasa una cadena
def extrae_mes(fecha):
    mes = fecha[3:5]
    return int(mes)

# Funcion que resolvera la tercer consigna sobre los ingresos totales anuales, mensuales
def tercer_consigna(productos,ventas):
    ventas_totales_por_year = []
    # Vamos a obtener los años de las ventas, para poder ir clasificando por año las venta
    years = regresa_años(ventas)
    # Para sacar la venta de un año debemos de primero sacar la cantidad del producto en cuestion
    # luego esa cantidad la multiplicamos por el precio del producto
    # Los productos que no tengan ventas de todas formas no afectaran la suma
    for year in years:
        total = 0
        for producto in productos:
            cantidad = 0
            for venta in ventas:
                # Extraemos el año de la venta en cuestion
                year_venta = extrae_año(venta[3])
                # Comparamos si la venta fue del producto en cuestion y comparamos si el año de la venta coincide
                # con nuestra lista con los años de nuestra BD
                if producto[0] == venta[1] and year == year_venta:
                    cantidad += 1
            # Vamos haciendo la suma por año
            total += cantidad * producto[2]
        # Una vez que se haya acabado de iterar sobre los productos podemos agregar en nuestra lista
        # una lista del año con el total respectivo
        ventas_totales_por_year.append([year,total])
    print(ventas_totales_por_year)
    print('\n')
    #A partir de aqui empezamos a ver las ventas por mes y por año
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    ventas_por_meses = []
    for year in years:
        for mes in meses:
            total = 0
            for producto in productos:
                cantidad = 0
                for venta in ventas:
                    year_venta = extrae_año(venta[3])
                    mes_venta = extrae_mes(venta[3])
                    if producto[0] == venta[1] and year == year_venta and mes == mes_venta:
                        cantidad += 1
                total += cantidad * producto[2]
            ventas_por_meses.append([mes,year,total])
    # Debemos de limpiar nuestra lista
    ventas_por_meses = limpia_lista(lista=ventas_por_meses,index=2,tamaño=len(ventas_por_meses))
    print(ventas_por_meses)
