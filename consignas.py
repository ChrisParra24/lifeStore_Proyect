from math import fsum
# Esta funcion nos sirve como parametro para ordenar por la cantidad de cada producto
def myKey(e):
    return e[1]

# Funcion que limpia la lista
def limpia_lista(lista):
    lista_limpia = []
    for elemento in lista:
        if elemento[1] != 0:
            lista_limpia.append(elemento)
    return lista_limpia

# Funcion que nos muestra los 10 productos con menores busquedas por categoria
def muestra_menores_busquedas(diccionario,categorias,tamaño):
    for categoria in categorias:
        print(f'\nPara la categoria {categoria} los {tamaño} menos buscados fueron:')
        lista = diccionario[categoria]
        lista.sort(key=myKey)
        lista = lista[:tamaño]
        if len(lista) == 0:
            print(f'Para la categoria "{categoria}" no hubo busquedas')
        else:
            for elemento in lista:
                print(f'El producto con id: {elemento[0]} con {elemento[1]} busquedas')
        
# Funcion que muestra los 10 productos con mayores busquedas
def muestra_mayores_busquedas(lista,tamaño):
    elementos = lista[:tamaño]
    print(f'\nLos {tamaño} productos mas buscados fueron:')
    for elemento in elementos:
        print(f'El producto con el id: {elemento[0]} con {elemento[1]} busquedas')

# Funcion que cuenta el numero de busquedas
def conteo_de_busquedas(productos,busquedas):
    busquedas_contabilizadas = []
    for producto in productos:
        contador = 0
        for  busqueda in busquedas:
            if producto[0] == busqueda[1]:
                contador += 1
        #guardamos el id_product, la cantidad, y la categoria
        busquedas_contabilizadas.append([producto[0],contador,producto[3]])
    busquedas_limpias = limpia_lista(busquedas_contabilizadas)
    busquedas_limpias.sort(key=myKey,reverse=True)
    return busquedas_limpias

# Funcion que extrae solo las categorias de los productos
def extrae_categorias(productos):
    categorias = []
    for producto in productos:
        if producto[3] not in categorias:
            categorias.append(producto[3])
    return categorias

#Funcion que nos categorizara los productos junto con sus respectivas cantidades
def productos_top(categorias,productos):
    diccionario = {}
    for categoria in categorias:
        if categoria not in diccionario.keys():
            diccionario[categoria] = []
            for producto in productos:
                if categoria == producto[2]:
                    diccionario[categoria].append([producto[0],producto[1]])
    return diccionario

# Funcion que muestra los 5 productos de cada categoria con mas ventas resultados
def muestra_primer_consigna_mas_ventas(productos_contabilizados,tamaño):
    lista = productos_contabilizados[:tamaño]
    print(f"\nLos {tamaño} productos con mayores ventas son:")
    for elemento in lista:
        print(f'El producto con id: {elemento[0]} con {elemento[1]} ventas')

#Funcion que nos muestra los 5 productos con menos ventas
def muestra_primer_consigna_menos_ventas(diccionario, categorias, palabra, tamaño):
    for categoria in categorias:
        print(f'\nEn la categoria de {categoria} los {tamaño} productos {palabra} fueron:')
        lista = diccionario[categoria]
        #acomodamos la lista en modo ascendente con base en la cantidad
        lista.sort(key=myKey)
        lista = lista[:tamaño]
        for elemento in lista:
            print(f'El producto con id: {elemento[0]} con {elemento[1]} piezas vendidas')

#Funcion que nos regresa las ventas sin las devoluciones
def ventas_sin_reembolso(ventas):
    ventas_sin_reembolso = []
    for venta in ventas:
        if venta[4] == 0:
            #guardamos el id_venta y el id_product
            ventas_sin_reembolso.append(venta[:4])
    return ventas_sin_reembolso

#Funcion que nos hace el conteo de nuestros productos vendidos
def conteo_productos(productos,ventas):
    productos_contabilizados = []
    for producto in productos:
        contador = 0
        for venta in ventas:
            if producto[0] == venta[1]:
                contador+=1
        # agregamos el id_producto, cantidad y ademas de su categoria
        productos_contabilizados.append([producto[0],contador,producto[3]])
    # acomodamos los productos
    productos_limpios_contabilizados = limpia_lista(productos_contabilizados)
    productos_limpios_contabilizados.sort(reverse=True,key=myKey)
    return productos_limpios_contabilizados
    
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

# Funcion que nos regresa los productos con sus calificaciones
def calificaciones_productos(productos,ventas):
    diccionario = {}
    for producto in productos:
        if producto[0] not in diccionario.keys():
            diccionario[producto[0]] = []
            for venta in ventas:
                if venta[1] == producto[0]:
                    diccionario[producto[0]].append(venta[2])
    return diccionario

# Funcion que nos calculara el promedio de reseñas de cada producto
def promedio_reseñas(diccionario):
    promedios = []
    for key in diccionario.keys():
        lista = diccionario[key]
        if len(lista) > 0:
            num_elementos = len(lista)
            prom = fsum(lista) / num_elementos
            frecuencia = lista.count(5)
            #guardamos el id producto,frecuencia(numero de veces que aparece el 5), promedio de reseñas
            promedios.append([key,frecuencia,prom])
    promedios.sort(key=myKey,reverse=True)
    return promedios

# Funcion que nos imprime los 5 productos con mas reseñas
def muestra_5_mejores_reseñas(lista,tamaño):
    lista_5_mejores = lista[:tamaño]
    print(f'\nLos {tamaño} con mejores reseñas son:')
    for elemento in lista_5_mejores:
        print(f'El producto con id: {elemento[0]} con {elemento[1]} calificaciones de 5 estrellas dando un promedio de su reseña de {elemento[2]}')
    return lista_5_mejores

# Funcion que nos imprime los 5 productos con peores reseñas
def muestra_5_peores_reseñas(lista,tamaño):
    lista.sort(key=myKey)
    lista_5_peores = lista[:tamaño]
    print(f'\nLos {tamaño} con peores reseñas son:')
    for elemento in lista_5_peores:
        print(f'El producto con id: {elemento[0]} con {elemento[1]} calificaciones de 5 estrellas dando un promedio de su reseña de {elemento[2]}')
    return lista_5_peores

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
                if producto[0] == venta[1] and year == year_venta and venta[4]==0:
                    cantidad += 1
            # Vamos haciendo la suma por año
            total += cantidad * producto[2]
        # Una vez que se haya acabado de iterar sobre los productos podemos agregar en nuestra lista
        # una lista del año con el total respectivo
        ventas_totales_por_year.append([year,total])
    print('Las ingresos por año son los siguientes:')
    for año in ventas_totales_por_year:
        print(f'El año {año[0]} tuvo ingresos de ${año[1]}')
    #A partir de aqui empezamos a ver las ventas por mes y por año
    meses = [[1,'Enero'],[2,'Febrero'],[3,'Marzo'],[4,'Abril'],[5,'Mayo'],[6,'Junio'],[7,'Julio'],[8,'Agosto'],[9,'Septiembre'],[10,'Octubre'],[11,'Noviembre'],[12,'Diciembre']]
    ventas_por_meses = []
    for year in years:
        for mes in meses:
            total = 0
            for producto in productos:
                cantidad = 0
                for venta in ventas:
                    year_venta = extrae_año(venta[3])
                    mes_venta = extrae_mes(venta[3])
                    if producto[0] == venta[1] and year == year_venta and mes[0] == mes_venta and venta[4]==0:
                        cantidad += 1
                total += cantidad * producto[2]
            ventas_por_meses.append([mes[1],total,year])
    # Debemos de limpiar nuestra lista
    ventas_por_meses = limpia_lista(lista=ventas_por_meses)
    print()
    print('Los ingresos que se tuvieron por mes son los siguientes: ')
    for venta_por_mes in ventas_por_meses:
        print(f'En {venta_por_mes[0]} del {venta_por_mes[2]} se tuvo ingresos por ${venta_por_mes[1]}')
    
    # Sacamos las ventas promedio mensual de cada año
    print()
    for year in ventas_totales_por_year:
        contador = 0
        for venta_por_mes in ventas_por_meses:
            if year[0] == venta_por_mes[2]:
                contador += 1
        if contador != 0:
            print(f'Las ventas promedio mensual en {year[0]} son de: ${year[1]/contador}')