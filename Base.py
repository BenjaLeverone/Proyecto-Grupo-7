contra_seña=["1245"]
gmailes=["falcondelacruzjulio@gmail.com"]
registros=[["julio","falcon","588255","feliz","245"]]
dinero=["500","500"]
#codigo de logeo#

def oficialcuenta(dato,co_traseña,g_mail,re_gistro,d_inero):
    print("ingrese un numero a base de los siguientes opciones: ")
    print("1:ver dinero disponible")
    print("2:cambiar contraseña")
    print("3:tranferencia")
    print("4:retirar dinero")
    print("5:pagar una cuenta")
    print("6:ingresar dinero")
    print("7:prestamos")
    print("si quiere salir escriba: salir ")
    opcion=input()
    if opcion=="1":
        datos_cuenta(dato,re_gistro,d_inero)

def datos_cuenta(cuenta_datos,re_gistross,dinero_verdes):
    print(f"-------------{re_gistross[cuenta_datos][0]}------------------")
    print(f"-------------{re_gistross[cuenta_datos][1]}-------------------")
    print(f" DNI: {re_gistross[cuenta_datos][2]}")
    print(f" Calle: {re_gistross[cuenta_datos][3]}")
    print(f" Direccion: {re_gistross[cuenta_datos][4]}")
    print(f" Dinero: {dinero_verdes[cuenta_datos]}")

def logearse(contr_aseñas,gmail_oficial,regi_tros,dine_ro):                                            #verificacion de datos de la cuenta
    gmail=input("Ingrese gmail: ").lower()
    contraseña=input("ingrese contraseña:")
    while verificacion_gmail(gmail,gmailes)!=True:
        print("comunicarse con el soporte si no puede ingresar")
        gmail=input("ingrese nuevamente gmail: ").lower()
    while verificacion(contraseña,contra_seña)!=True:
        contraseña=input("si se olvideo la contraseña ingrese -1\ningrese contraseña : ")
        if contraseña=="-1":
            recuperacion(gmail,gmail_oficial)
    indice=gmail_oficial.index(gmail)
    oficialcuenta(indice,contr_aseñas,gmail_oficial,regi_tros,dine_ro)
        
def verificacion(cuenta_n,contraseñas):
    b=False                                 #verificacion de contraseña
    for numeros in contraseñas:             #verifica que la contraseña sea valido 
        if cuenta_n==numeros:
            b=True
    return b

def verificacion_gmail(gmail_m,lista):          #verificacion de gmail        
    a=False                                     #verifica que el gmail existe en la lista
    for palabras in lista:
        if gmail_m==palabras:
            a=True
    return a

def recuperacion(posicion,gmail_oficialmente):                          #recuperacion de contraseña
    codigo=input("ingrese codigo: ")               
    nueva=input("ingrese nueva contraseña:")                      
    nueva2=input("ingrese nuevamente contraseña para verificar: ")
    posicionn=gmail_oficialmente.index(posicion)
    if nueva==nueva2:
        contra_seña.pop(posicionn)
        contra_seña.insert(posicionn,nueva2)

#codigo de registro#
def registrado(contra,ggmail,registros_dos,dinero_moneda):                                                 
    print("felicidades se registro correctamente")
    print("si desea ingresar seleccione 1 ")
    print("si desea salir ingrese 2")
    numero=int(input())
    if numero==1:
        logearse(contra,ggmail,registros_dos,dinero_moneda)
    if numero==2:
        main()

def verificacion_dni(numeros):                       #verifica que el dni sea un dni valido
    while int(numeros)<1000000 or int(numeros)>100000000:
            numeros=input("por favor ingrese dni valido\ningrese dni: ")
    return numeros

def verifiacion_gmailcom(gmail_n,gmails):
    verifiacion_completa=gmail_norepetido(gmail_n,gmails)                                                      #comprueba que el gmail sea valido#
    while "@gmail.com" not in gmail_n or verifiacion_completa!=True:
        gmail_n=input("ingrese gmail valido\npuede ser que el gmail ingresado ya esta registrado verifique : ").lower()
        verifiacion_completa=gmail_norepetido(gmail_n,gmails)
    return gmail_n

def gmail_norepetido(gmail_d,gmail_lista):
    bb=True
    if gmail_d in gmail_lista:
        bb=False
    return bb


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
        logearse(contra_seña,gmailes,registros,dinero)
    if numero=="2":
        nombre=input("ingrese nombre: ").lower() 
        apellido=input("ingrese apellido: ").lower() 
        dni=verificacion_dni(input("ingrese numero de dni: "))
        direccion=input("ingrese calle : ").lower()
        numero_direccion=input("ingrese numero de direccion: ")
        registros.append([nombre,apellido,dni,direccion,numero_direccion])      
        gmail_nuevo=verifiacion_gmailcom(input("ingrese gmail: ").lower(),gmailes)  #se puede usar map
        gmailes.append(gmail_nuevo)
        contra_seña.append(input("ingrese contraseña: "))
        registrado(contra_seña,gmailes,registros,dinero)
    if numero=="salir":
        print("fin del programa")
main()