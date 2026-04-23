registros=[{"nombre":"julio",
            "apellido":"falcon",
            "dni":12345678,
            "nombre_calle":"calle",
            "direccion":123,
            "telefono":12345678900,
            "gmail":"falcondela@gmail.com",
            "contraseña":12345,
            "dinero":0}]
            
#codigo de logeo#

def oficialcuenta(registro_informacion):
    print()
    print("-------------------------------------------------------------")
    print("ingrese un numero a base de los siguientes opciones: ")
    print("1:informacion personal")
    print("2:cambiar contraseña")
    print("3:tranferencia")
    print("4:retirar dinero")
    print("5:pagar una cuenta")
    print("6:ingresar dinero")
    print("7:prestamos")
    print("si quiere salir escriba: salir ")
    print("---------------------------------------------------------------")
    opcion=input()
    if opcion=="1":
        datos_cuenta(registro_informacion)
def datos_cuenta(datos_cliente):
    print(f"nombre : {datos_cliente["nombre"]}")
    print(f"apellido : {datos_cliente["apellido"]}")
    print(f"dni : {datos_cliente["dni"]}")
    print(f"calle : {datos_cliente["nombre_calle"]}")
    print(f"numero de direccion : {datos_cliente["direccion"]}")
    print(f"numero de telefono : {datos_cliente["telefono"]}")
    print(f"gmail : {datos_cliente["gmail"]}")
    print(f"dinero disponible : {datos_cliente["dinero"]}")


def logearse(datos): 
    cliente_datos="algo"                                      #verificacion de datos de la cuenta
    while True:
        encontrado=False
        gmail_registrado=input("Ingrese gmail: ").lower()
        contraseña_registrado=input("ingrese contraseña:")
        for clave in datos:
            if clave["gmail"]==gmail_registrado and clave["contraseña"]==contraseña_registrado:
                encontrado=True
                cliente_datos=clave
        if encontrado:
            break
        else:
            print("gmail o contraseña incorrecta\nverifique por favor ")
    oficialcuenta(cliente_datos)

#codigo de registro#
def registrado(registros_d):                                                 
    print("felicidades se registro correctamente")
    print("si desea ingresar seleccione 1 ")
    print("si desea salir ingrese 2")
    numero=int(input())
    if numero==1:
        logearse(registros_d)
    if numero==2:
        main()

def verificacion_dni(numeros):
    while numeros<1000000 or numeros>100000000:
            numeros=int(input("ingrese numero de dni valido: "))
    return numeros

def verifiacion_gmailcom(gmail_n):                                                      #comprueba que el gmail sea valido#
    while "@gmail.com" not in gmail_n:
        gmail_n=input("ingrese gmail valido: ").lower()
    return gmail_n

def verificacion_telefono(numero):
    while numero<1000000000 or numero>10000000000:
        numero=int(input("ingrese numero de telefono valido : "))
    return numero 

#programa principal#
def main():
    print("-----------Bienvenido a billetera virtual----------")
    print()
    print("-----------para logearse ingrese; 1 : ")
    print()
    print("-----------para crear una cuenta ingrese; 2 : ")
    print()
    print("-----------si desea salir escriba: salir ")
    numero=input()
    if numero=="1":
        logearse(registros)
    if numero=="2":
        registros_datos={}
        registros_datos["nombre"]=input("ingrese nombre: ").lower() 
        registros_datos["apellido"]=input("ingrese apellido: ").lower() 
        registros_datos["dni"]=verificacion_dni(int(input("ingrese numero de dni: ")))
        registros_datos["nombre_calle"]=input("ingrese calle : ").lower()
        registros_datos["direccion"]=int(input("ingrese numero de direccion: "))
        registros_datos["telefono"]=verificacion_telefono(int(input("ingrese numero de telefono: ")))
        registros_datos["gmail"]=verifiacion_gmailcom(input("ingrese gmail: ")).lower()
        registros_datos["contraseña"]=input("ingrese contraseña: ")
        registros_datos["dinero"]=0
        for clave in registros:
            while registros_datos["dni"]==clave["dni"]:
                registros_datos["dni"]=verificacion_dni(int(input("el dni ingresado esta registrado a otra cuenta\ningrese otro dni:")))
            while registros_datos["gmail"]==clave["gmail"]:
                registros_datos["gmail"]=verifiacion_gmailcom(input("el gmail ingresado esta registrado a otra cuenta , ingrese otro gmail: "))
            while registros_datos["telefono"]==clave["telefono"]:
                registros_datos["telefono"]=verificacion_telefono(int(input("el numero ingresado esta registrado a otra cuenta\ningrese numero de telefono: ")))
        registros.append(registros_datos)
        registrado(registros)                                                                                                                                                                                                         
    if numero=="salir":
        print("fin del programa")
main()