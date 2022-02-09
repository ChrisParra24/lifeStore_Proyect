#importamos nuestra pequeña BD que esta en el archivo lifestore_file.py
from lifestore_file import lifestore_products,lifestore_sales,lifestore_searches
# Estos son los datos de nuestra BD:
# lifestore_searches = [id_search, id product]
# lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
# lifestore_products = [id_product, name, price, category, stock]

from consignas import calificaciones_productos, conteo_productos, muestra_menores_busquedas, muestra_primer_consigna_mas_ventas, muestra_primer_consigna_menos_ventas, productos_top, promedio_reseñas, tercer_consigna, ventas_sin_reembolso,extrae_categorias,conteo_de_busquedas,muestra_mayores_busquedas

########################################################################################################################
# Definimos los usuarios y contraseñas que podrán acceder a nuestro sistema de Gerencia de Venta
# Definimos una bandera = False que nos servira para saber si se encontro al usuario que intenta ingresar
# Definimos la variable estado_programa = 'ejecutando' para ciclar el inicio de sesion
# Definimos la variable mensaje_bienvenida para poder dar un mensaje de bienvenida en nuestro programa
# Definimos la variable mensaje_despedida para poder despedirnos del usuario
lista_usuarios = [
    ['christiam','lagunes1234'],
    ['jimmy', 'ymmij']
]
bandera = False
estado_programa = 'ejecutando'
mensaje_bienvenida = '\nBienvenido a Gerencia de Venta\n¡Accede con tus credenciales por favor!'
mensaje_despedida = '¡Hasta pronto!'


# Empezamos el ciclo para poder iniciar sesion
while estado_programa == 'ejecutando':
    print(mensaje_bienvenida)
    user_name = input('Usuario: ')
    password = input('Contraseña: ')
    for usuario in lista_usuarios:
        if user_name in usuario and password in usuario:
            bandera = True
            break
    if bandera==True:
        productos_vendidos_cantidad = []
        productos_buscados_cantidad = []
        # Aqui entramos al programa de Gerencia de Venta y debemos de poder crear nuestros reportes y estrategias
        # Hacemos un menu iterativo de nueva forma y hacemos uso de la variable estado_programa para que el mismo usuario sea
        # capaz de elegir que reporte quiere ver
        print('\n\n¡Bienvenido ' + user_name + '!\n')
        while estado_programa == 'ejecutando':
            print('\nMenu Gerencia de Venta\n1.-Productos más vendidos y productos rezagados\n2.-Productos por reseña de servicio\n3.-Total de ingresos y ventas\n4.-Salir')
            opcion = int(input('Digite el numero de su elección: '))
            if opcion == 1:
                #-------------------------------ventas---------------------------------------------
                ventas = ventas_sin_reembolso(lifestore_sales)
                productos_ya_contados = conteo_productos(lifestore_products,ventas)
                categorias = extrae_categorias(lifestore_products)
                mis_productos_clasificados = productos_top(categorias,productos_ya_contados)
                #impresion de las ventas
                muestra_primer_consigna_mas_ventas(productos_ya_contados,5)
                muestra_primer_consigna_menos_ventas(mis_productos_clasificados,categorias,'menos vendidos',5)
                #--------------------------busquedas------------------------------------------
                productos_con_busquedas = conteo_de_busquedas(lifestore_products,lifestore_searches)
                muestra_mayores_busquedas(productos_con_busquedas,10)
                diccionario_busquedas = productos_top(categorias=categorias,productos = productos_con_busquedas)
                muestra_menores_busquedas(diccionario=diccionario_busquedas,categorias=categorias,tamaño=10)
            elif opcion == 2:
                productos_con_reseñas = calificaciones_productos(lifestore_products,lifestore_sales)
                productos_con_promedios = promedio_reseñas(productos_con_reseñas)
                print(productos_con_promedios)
            elif opcion == 3:
                tercer_consigna(lifestore_products,lifestore_sales)
            elif opcion == 4:
                print(f"\n{mensaje_despedida}")
                exit()
            else:
                print('Seleccione una opcion valida')
            
    else:
        #preguntamos si va a intentar de nuevo entrar al sistema
        estado_programa = input('No son correctas las credenciales\n¿Desea intentar de nuevo? (si/no): ')
        if estado_programa == 'no':
            #nos salimos del programa
            print(f"\n{mensaje_despedida}")
        else:
            #seguimos dentro del programa y vuelve a pedir el usuario y la contraseña
            estado_programa = 'ejecutando'
