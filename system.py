programa1 = "Java de Cero a Senior "
programa2 = "Python con IA Aplicada"
programa3 = "Mobile Senior con IA"
estudiantes1 = 0
estudiantes2 = 0
estudiantes3 = 0
precioPrograma = 1800000.0


def menuSistema():
    print("\n ----Bienvenido al Sistema de Ventas----")
    print("1. Mostrar los programas disponibles")
    print("2. Registrar la venta de cualquiera de los tres programas")
    print("3. Consultar los ingresos acomulados por cada programa")
    print("4. Mostrar el total general de los ingresos del dia")
    print("5. Salir del sistema")
        
def mostrarProgramas():
    print("\n ****Programas Disponibles****")
    print(f"1. {programa1} y tiene un valor de {precioPrograma:,.0f}")
    print(f"2. {programa2} y tiene un valor de {precioPrograma:,.0f}")
    print(f"3. {programa3} y tiene un valor de {precioPrograma:,.0f}")
        
        
def registrarVenta():
    global programa1, programa2, programa3, estudiantes1, estudiantes2, estudiantes3
    print(f"1. {programa1}")
    print(f"2. {programa2}")
    print(f"3. {programa3}")
    
    opcion = int(input("Seleccione el programa a vender: "))
    
    if opcion == 1:
        estudiantes1 += 1
        print(f"¡Programa vendido! Hay {estudiantes1} estudiantes en {programa1}")
    elif opcion == 2:
        estudiantes2 += 1
        print(f"¡Programa vendido! Hay {estudiantes2} estudiantes en {programa2}")
    elif opcion == 3:
        estudiantes3 += 1
        print(f"¡Programa vendido! Hay {estudiantes3} estudiantes en {programa3}")
    else:
        print("Error seleccione un programa valido!")
        
def ingresosAcomulados():
    global programa1, programa2, programa3
    print(f"1. {programa1}")
    print(f"2. {programa2}")
    print(f"3. {programa3}")
    
    opcion = int(input("De cual programa deseas consultar los ingresos?: "))
    
    if opcion == 1:
        total_acomulado = precioPrograma * estudiantes1
        print(f"Los ingresos de {programa1} son: {total_acomulado:,.0f}")
        
    elif opcion == 2:
        total_acomulado = precioPrograma * estudiantes2
        print(f"Los ingresos de {programa2} son: {total_acomulado:,.0f}")
        
    elif opcion == 3:
        total_acomulado = precioPrograma * estudiantes3
        print(f"Los ingresos de {programa3} son: {total_acomulado:,.0f}")
    else:
        print("Error seleccione un programa valido o escriba un entero y no una letra")
    
def ingresosDia ():
    total_estudiantes = estudiantes1 + estudiantes2 + estudiantes3
    total_ingresos = precioPrograma * total_estudiantes
    print(f"Los ingresos del dia son: ${total_ingresos:,.0f} pesos colombianos")
    
def salirSistema():
    print("\n Gracias por usar nuestro sistema! :)")
    
    
while True:
    menuSistema()
    opcion = int(input("Seleccion una opcion: "))
    
    if opcion == 1:
        mostrarProgramas()
    elif opcion == 2:
        registrarVenta()
    elif opcion == 3:
        ingresosAcomulados()
    elif opcion == 4:
        ingresosDia ()
    elif opcion == 5:
        salirSistema()
        break
    else:
        print("Error seleccione una opcion valida!")
        break