#importamos nuestra pequeña BD que esta en el archivo lifestore_file.py
from lifestore_file import lifestore_products,lifestore_sales,lifestore_searches
# Estos son los datos de nuestra BD:
# lifestore_searches = [id_search, id product]
# lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
# lifestore_products = [id_product, name, price, category, stock]

from consignas import calificaciones_productos, conteo_productos, muestra_5_mejores_reseñas, muestra_5_peores_reseñas, muestra_menores_busquedas, muestra_primer_consigna_mas_ventas, muestra_primer_consigna_menos_ventas, productos_top, promedio_reseñas, tercer_consigna, ventas_sin_reembolso,extrae_categorias,conteo_de_busquedas,muestra_mayores_busquedas

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
    # Pedimos al usuario que ingrese su usario
    user_name = input('Usuario: ')
    # Pedimos al usuario que ingrese contraseña para poder verificar que este en nuestra lista de usuarios
    password = input('Contraseña: ')
    for usuario in lista_usuarios: # Iteramos sobre la lista_usuarios para poder verificar que la persona que esta intentando logear pues si sea alguien de la lista (autenticacion)
        if user_name in usuario and password in usuario: # Comparamos los datos y en caso de que este cambiamos la bandera a True para darle acceso al menu de la Gerencia de venta
            bandera = True
            break # Si lo encontramos hacemos que deje de buscar en lo que resta de la lista_usuarios
    if bandera==True:
        # Aqui entramos al programa de Gerencia de Venta y debemos de poder crear nuestros reportes y estrategias
        # Hacemos un menu iterativo de nueva forma y hacemos uso de la variable estado_programa para que el mismo usuario sea
        # capaz de elegir que reporte quiere ver
        print('\n\n¡Bienvenido ' + user_name + '!\n')
        while estado_programa == 'ejecutando':
            print('\nMenu Gerencia de Venta\n1.-Productos más vendidos y productos rezagados\n2.-Productos por reseña de servicio\n3.-Total de ingresos y ventas\n4.-Salir')
            opcion = int(input('Digite el numero de su elección: '))
            if opcion == 1:
                #-------------------------------ventas---------------------------------------------
                # Primero obtendremos todas las ventas sin contar las devoluciones
                ventas = ventas_sin_reembolso(lifestore_sales)
                # Despues obtenemos el conteo de productos, es decir, los productos con sus respectivas cantidad de ventas
                productos_ya_contados = conteo_productos(lifestore_products,ventas)
                # Obtenemos las categorias para poder despues hacer uso de ellas y poder clasificar las ventas y busquedas
                categorias = extrae_categorias(lifestore_products)
                # Aqui ya solo obtenemos un diccionario con las categoria como clave y dentro de ellas una lista con los productos y sus respectiva informacion
                mis_productos_clasificados = productos_top(categorias,productos_ya_contados)
                #impresion de las ventas - tanto los 5 productos con mayor venta como por categoria los 5 menos vendidos
                muestra_primer_consigna_mas_ventas(productos_ya_contados,5)
                muestra_primer_consigna_menos_ventas(mis_productos_clasificados,categorias,'menos vendidos',5)
                #--------------------------busquedas------------------------------------------
                # Obtenemos los productos con la cantidad de busquedas que tuvieron
                productos_con_busquedas = conteo_de_busquedas(lifestore_products,lifestore_searches)
                # Mostramos los 10 productos con mayores busquedas
                muestra_mayores_busquedas(productos_con_busquedas,10)
                # Obtenemos un diccionario con las categorias como claves y cada clave con una lista con los productos que pertenecen a esa categoria con su respectiva informacion
                diccionario_busquedas = productos_top(categorias=categorias,productos = productos_con_busquedas)
                # Mostramos por categoria los 5 productos con menos busquedas de cada categoria, no se da en todos los productos que tengan 10 busquedas
                muestra_menores_busquedas(diccionario=diccionario_busquedas,categorias=categorias,tamaño=10)
            elif opcion == 2: # Si el usuario logeado selecciona la opcion 2 del menu entonces se le mostraran los productos con mejor y peor reseña (solo 5)
                # Aqui lo que hacemos es obtener un diccionario con los id_product como clave y con las reseñas que tiene
                productos_con_reseñas = calificaciones_productos(lifestore_products,lifestore_sales)
                # Aqui obtenemos los promedios de cada producto y los guardamos en una lista
                productos_con_promedios = promedio_reseñas(productos_con_reseñas)
                # Aqui obtenemos la lista con los 5 productos con mejor reseña y también los mostramos en pantalla, es por eso que mandamos parametros, la lista y el tamaño de cuantos productos debe de mostrar
                productos_5_mas_reseñas = muestra_5_mejores_reseñas(productos_con_promedios,5)
                # Aqui obtenemos la lista con los 5 productos con peor reseña y también los mostramos en pantalla, es por eso que mandamos parametros, la lista y el tamaño de cuantos producltos deben de mostrar
                productos_5_peor_reseña = muestra_5_peores_reseñas(productos_con_promedios,5)
            elif opcion == 3: # Si el usuario logeado selecciona la opcion 3 del menu entonces se le mostraran las ventas totales por año, por mes y las ventas promedio mensual
                # Simplemente llamamos a la funcion tercer consigna que se encarga de hacer las operaciones y de mostrar la información que se solicita
                tercer_consigna(lifestore_products,lifestore_sales)
            elif opcion == 4: # Si el usuario logeado presiona 4 entonces podrá salir de la ejecución del sistema, es decir, se sale del programa
                print(f"\n{mensaje_despedida}")
                exit()
            else:
                # En caso de seleccionar una opcion invalida se volvera a mostar el menu y tendrá que verse forzado a elegir una opción o salir del programa
                print('Seleccione una opcion valida')
            
    else:
        #preguntamos si va a intentar de nuevo entrar al sistema despues de haberse equivocado con las credenciales
        estado_programa = input('No son correctas las credenciales\n¿Desea intentar de nuevo? (si/no): ')
        if estado_programa == 'no':
            #nos salimos del programa
            print(f"\n{mensaje_despedida}")
        else:
            #seguimos dentro del programa y vuelve a pedir el usuario y la contraseña
            estado_programa = 'ejecutando'
