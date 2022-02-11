# Importamos del modulo math la funcion fsum para poder hacer la suma de los elementos de una lista
from math import fsum
# Esta funcion nos sirve como parametro para ordenar por la cantidad de cada producto o por lo que haya en una lista en la posicion 1
def myKey(e):
    return e[1]

# Funcion que limpia la lista si lo que haya en las sublistas en la posicion 1 es igual a 0, esto para no tener que regresar datos que tienen 0
def limpia_lista(lista):
    lista_limpia = []
    for elemento in lista:
        if elemento[1] != 0:
            lista_limpia.append(elemento)
    return lista_limpia

# Funcion que nos muestra los 10 productos con menores busquedas por categoria
def muestra_menores_busquedas(diccionario,categorias,tamaño):
    for categoria in categorias: # Iteramos sobre las categorias
        print(f'\nPara la categoria {categoria} los {tamaño} menos buscados fueron:')
        lista = diccionario[categoria] # extraemos la lista que haya en el diccionario con la clave = categoria
        lista.sort(key=myKey) # ordenamos esa lista de manera ascendente de acuerdo a lo que haya en la posicion 1
        lista = lista[:tamaño] # Obtenemos la cantidad de productos que vamos a mostrar, en este caso los que tengan menores busquedas
        if len(lista) == 0: # Si no tiene nada la lista, entonces no hubo ninguna busqueda de ningun producto de esa categoria
            print(f'Para la categoria "{categoria}" no hubo busquedas')
        else:
            for elemento in lista: #iteramos sobre la lista ordenada ascendentemente y vamos imprimiendo el id_product y la cantidad de busquedas que tuvo
                print(f'El producto con id: {elemento[0]} con {elemento[1]} busquedas')
        
# Funcion que muestra los 10 productos con mayores busquedas
def muestra_mayores_busquedas(lista,tamaño):
    elementos = lista[:tamaño]
    print(f'\nLos {tamaño} productos mas buscados fueron:')
    for elemento in elementos: # Iteramos sobre los elementos que hay en la lista e imprimimos la informacion correspondiente
        print(f'El producto con el id: {elemento[0]} con {elemento[1]} busquedas')

# Funcion que cuenta el numero de busquedas que tiene un producto
def conteo_de_busquedas(productos,busquedas):
    busquedas_contabilizadas = [] # lista que nos servira para poder guardar informacion de un producto
    for producto in productos: #iteramos sobre los productos
        contador = 0 # inicializamos el contador en 0 para cada producto
        for  busqueda in busquedas: # Iteramos sobre la lista de busquedas
            if producto[0] == busqueda[1]: # comparamos que el producto haya estado en la lista de busquedas, es decir, el id_product debe de coincidir en ambas listas
                contador += 1 #incrementamos el contador
        #guardamos el id_product, la cantidad, y la categoria
        busquedas_contabilizadas.append([producto[0],contador,producto[3]])
    # aqui lo que hacemos es limpiar la lista, quitamos los productos que hayan tenido 0 busquedas
    busquedas_limpias = limpia_lista(busquedas_contabilizadas)
    # ordenamos la lista de manera descendente mediante la cantidad que haya tenido de busquedas
    busquedas_limpias.sort(key=myKey,reverse=True)
    # regresamos la lista limpia y ordenada
    return busquedas_limpias

# Funcion que extrae solo las categorias de los productos
def extrae_categorias(productos):
    categorias = []
    for producto in productos: #iteramos sobre los productos
        if producto[3] not in categorias: # checamos que no este la categoria en nuestra lista que guarda las categorias
            categorias.append(producto[3]) # si no esta, entonces agregamos la categoria a la lista
    #retornamos las categorias de los productos sin repetir
    return categorias

# Funcion que nos categorizara los productos junto con sus respectivas cantidades
# Aqui los productos que entran como parametro ya estan limpios, es decir, tienen el id_product, la cantidad de ventas que tienen
def productos_top(categorias,productos):
    diccionario = {}
    for categoria in categorias: #iteramos sobre las categorias
        if categoria not in diccionario.keys(): # si la categoria no esta en el diccionario como clave entonces
            diccionario[categoria] = [] # creamos la clave y también le decimos que esa clave corresponde a una lista
            for producto in productos: # iteramos sobre los productos
                if categoria == producto[2]: # Comparamos si la categoria es igual a la del producto en cuestion
                    diccionario[categoria].append([producto[0],producto[1]]) # si es entonces guardamos en la lista que esta en el diccionario el id product y la cantidad
    #retornamos el diccionario con la informacion
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
        lista.sort(key=myKey) # ordenamos la lista de manera ascendente con respecto al primero elemento
        lista = lista[:tamaño] # solo tomamos los elementos que necesitamos ya que esta ordenada
        for elemento in lista: # Iteramos sobre los elementos de la lista e imprimimos la información
            print(f'El producto con id: {elemento[0]} con {elemento[1]} piezas vendidas')

#Funcion que nos regresa las ventas sin las devoluciones
def ventas_sin_reembolso(ventas):
    ventas_sin_reembolso = []
    for venta in ventas: # Iteramos sobre la lista de las ventas
        if venta[4] == 0: # Checamos que la venta no tenga devolucion
            #guardamos el id_venta y el id_product
            ventas_sin_reembolso.append(venta[:4])
    #regresamos las ventas sin devoluciones
    return ventas_sin_reembolso

#Funcion que nos hace el conteo de nuestros productos vendidos
# las ventas que recibe como parametro son ya las ventas sin devoluciones
def conteo_productos(productos,ventas):
    productos_contabilizados = []
    for producto in productos: # Iteramos sobre los productos
        contador = 0 # Inicializamos el contador en cero por cada producto
        for venta in ventas: # Iteramos sobre las ventas
            if producto[0] == venta[1]: # Checamos que coincidan el id_product de ambas listas
                contador+=1 # Aumentamos por cada venta que aparezca de ese producto
        # agregamos el id_producto, cantidad y ademas de su categoria
        productos_contabilizados.append([producto[0],contador,producto[3]])
    # Limpiamos los productos, es decir, que la lista no contenga aquellos que tienen 0 ventas y acomodamos los productos de manera descendente
    productos_limpios_contabilizados = limpia_lista(productos_contabilizados)
    productos_limpios_contabilizados.sort(reverse=True,key=myKey)
    # regresamos los productos limpios y ordenados
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
    for producto in productos: # iteramos sobre los productos
        if producto[0] not in diccionario.keys(): # checamos si no esta el id_product como clave en el diccionario
            diccionario[producto[0]] = [] # de ser asi creamos la clave y tambien una lista en esa clave
            for venta in ventas: # iteramos sobre las ventas
                if venta[1] == producto[0]: # checamos que coincida el id_product de los elementos en cuestion
                    diccionario[producto[0]].append(venta[2]) # si coincide entonces agregamos la reseña
    # regresamos el diccionario
    return diccionario

# Funcion que nos calculara el promedio de reseñas de cada producto
def promedio_reseñas(diccionario):
    promedios = []
    for key in diccionario.keys(): # iteramos sobre cada producto ya que la key es el id_product 
        lista = diccionario[key] # Extraemos la lista que tiene esa clave
        if len(lista) > 0: # verificamos que la longitud de la lista sea mayor de 0, es decir que tenga reseñas
            num_elementos = len(lista) # obtenemos el numero de elementos que tiene la lista
            prom = fsum(lista) / num_elementos # Sacamos el promedio de esa lista haciendo uso de la funcion fsum() que en automatico nos hace la suma de los elementos de una lista
            frecuencia = lista.count(5) # Sacamos el número de veces que aparece la reseña 5 en la lista
            #guardamos el id producto,frecuencia(numero de veces que aparece el 5), promedio de reseñas
            promedios.append([key,frecuencia,prom])
    # Acomodamos la lista promedios con base en la frecuencia de manera descendente
    promedios.sort(key=myKey,reverse=True)
    # retornamos la lista
    return promedios

# Funcion que nos imprime los 5 productos con mas reseñas
def muestra_5_mejores_reseñas(lista,tamaño):
    lista_5_mejores = lista[:tamaño]
    print(f'\nLos {tamaño} con mejores reseñas son:')
    for elemento in lista_5_mejores: # Iteramos sobre la lista y vamos imprimiendo su informacion, el id_product, la frecuencia y el promedio de sus reseñas
        print(f'El producto con id: {elemento[0]} con {elemento[1]} calificaciones de 5 estrellas dando un promedio de su reseña de {elemento[2]}')
    #regresamos esos mejores productos con reseñas 
    return lista_5_mejores

# Funcion que nos imprime los 5 productos con peores reseñas
def muestra_5_peores_reseñas(lista,tamaño):
    lista.sort(key=myKey) # Ordenamos la lista de manera ascendente con base en su frecuencia
    lista_5_peores = lista[:tamaño] # Extraemos los productos en otra lista
    print(f'\nLos {tamaño} con peores reseñas son:')
    for elemento in lista_5_peores: # Iteramos sobre la lista y vamos imprimiendo su información, id_product, la frecuencia y el promedio de sus reseñas
        print(f'El producto con id: {elemento[0]} con {elemento[1]} calificaciones de 5 estrellas dando un promedio de su reseña de {elemento[2]}')
    # Regresamos los 5 peores productos con base en su reseña
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
    for year in years: # Iteramos sobre los años
        for mes in meses: # Itermaos sobre los meses
            total = 0 # Inicializamos el total por mes en 0
            for producto in productos: # iteramos sobres los productos
                cantidad = 0 # Inicializamos el contador en 0 por cada producto
                for venta in ventas: # Iteramos sobre las ventas
                    year_venta = extrae_año(venta[3]) # obtenemos el año de la venta en cuestion
                    mes_venta = extrae_mes(venta[3]) # Obtenemos el mes de la venta en cuestion
                    # Comparamos si el producto conincide con el de la venta en cuestion y si el año coincide y si el mes tambien coincide y si la venta no es una devolucion
                    if producto[0] == venta[1] and year == year_venta and mes[0] == mes_venta and venta[4]==0:
                        cantidad += 1 # Sumamos la cantidad, para tener el numero de ventas en ese año y en ese mes de un producto
                total += cantidad * producto[2] # Obtenemos la cantidad total de ventas por producto
            # agregamos en nuestra lista una lista con: el mes, el total y el año
            ventas_por_meses.append([mes[1],total,year])
    # Debemos de limpiar nuestra lista
    # limpiamos la lista, quitamos aquellos que tengan total de 0
    ventas_por_meses = limpia_lista(lista=ventas_por_meses)
    print()
    print('Los ingresos que se tuvieron por mes son los siguientes: ')
    for venta_por_mes in ventas_por_meses: # Iteramos sobre la lista y vamos imprimiendo el mes, el año y la cantidad que se vendio en ese mes
        print(f'En {venta_por_mes[0]} del {venta_por_mes[2]} se tuvo ingresos por ${venta_por_mes[1]}')
    
    # Sacamos las ventas promedio mensual de cada año
    print()
    for year in ventas_totales_por_year: # Iteramos sobre los años con sus respectivas cantidades que se vendieron en ese año
        contador = 0 # Inicializamos el contador en 0 que nos ayudara a saber cuantos meses hubo ventas
        for venta_por_mes in ventas_por_meses: # Iteramos sobre la lista que tiene el mes, año y total
            if year[0] == venta_por_mes[2]:  # checamos que coincidan los años de ambas listas
                contador += 1 # Incrementamos el contador
        if contador != 0: # Si el contador es distinto de 0 entonces si hubo al menos un mes en el año con ventas
            print(f'Las ventas promedio mensual en {year[0]} son de: ${year[1]/contador}') # imprimimos las ventas promedio mensual del año