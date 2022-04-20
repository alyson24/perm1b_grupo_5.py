# Cajero automatico
Este programa tiene como función ser un cajero automático en el cual primero debes de colocar tu contraseña después desde el menú de opciones puedes retirar, ver tu saldo y salir. Al elegir la opción retirar te ofrece varias opciones preestablecidas incluyendo una opción de monto personalizado, una vez retirado el dinero se podrá observar tu saldo actual automáticamente al final podrás salir del cajero y volver a colocar la contraseña para reingresar; antes de retirar también se puede observar el saldo que tengas.
Por ejemplo:
1.	Te pide ingresar tu contraseña que es 1313
2.	Después podemos seleccionar la opción “6: Retirar otro monto”, ingresamos el monto de: 600 y automáticamente aparece el saldo actual que es 9400
3.	Y se reinicia el programa regresa para poner la contraseña

#Variables
contraseña=1313   
saldo=10000 
"Contraseña correcta
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
#A todos los montos se les puso una variable "str" y automaticamenete se le resta el monto y aparece el saldo actual; tambien el retiro no puede ser mayor al saldo 
               str=input('Ingrese su monto: ')
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
#opcion dos para ver el saldo                                                            
            elif O==2:                                          
                print("Usted tiene un saldo de: " +str(saldo))
                break; 
#opcion para salir del cajero
            elif O==3:                                
                print("Gracias vuelva pronto")
                break; 
#Contraseña incorrecta en el caso si es incorrecto puedes volver  a poner la cprrecta
    else:
        print("Contraseña incorrecto")            
