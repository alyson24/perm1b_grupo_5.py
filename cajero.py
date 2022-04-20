from asyncio import ReadTransport
#Variables
contraseña=1313
saldo=10000
#Contraseña correcta 
while True:
    C=int(input("Escriba la contraseña: "))
    if C==contraseña:
        print("--------MENÚ--------")
        print(" 1: Retirar")
        print(" 2: Ver saldo")
        print(" 3: Salir")
        while True:
            O=int(input("Seleccione una opcion: "))
            if O==1:
                print("MONTO QUE DESEA RETIRAR")
                print(" 1: 20")
                print(" 2: 50")
                print(" 3: 100")
                print(" 4: 150")
                print(" 5: 500")
                print(" 6: Ingrese otro monto")
                str=input('Ingrese su monto: ')
#En cada monto se puso una varibale "str" y se le resta el monto automaticamente aparece el saldo restante; el retiro no puede ser mayor al saldo
                if str == "1":
                   print("retiro realizado con exito --- saldo actual", saldo - 20)
                   break; 
                elif str == '2':
                   print("retiro realizado con exito --- saldo actual", saldo - 50)
                   break; 
                elif str == '3': 
                    print("retiro realizado con exito --- saldo actual", saldo - 100)
                    break; 
                elif str == '4':
                    print("retiro realizado con exito --- saldo actual", saldo - 150)
                    break; 
                elif str == '5':
                    print("retiro realizado con exito --- saldo actual", saldo - 500)
                    break; 
                elif str == '6':
                    rtr = int (input("Ingrese monto a retirar: "))
                    if saldo >= rtr:
                        print("Retiro realizado con exito")
                        print("Saldo actual", saldo - rtr)
                    if saldo <= rtr:
                        print("Monto invalido") 
                    break;  
 #Ver saldo
            elif O==2:
                print("Usted tiene un saldo de: " +str(saldo))
                break; 
 #Salir               
            elif O==3:
                print("Gracias vuelva pronto")
                break; 
 #Contraseña incorrecta si esta mal se vuelve a pedir la correcta 
    else:
        print("Contraseña incorrecto")
        

