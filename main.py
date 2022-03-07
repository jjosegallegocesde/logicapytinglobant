#logica con python


#Ejemplo 1 Hidroituango
'''nivelAgua=float(input("digita el nivel de agua: "))
if(nivelAgua>0 and nivelAgua<200):
    print("la represa tiene poca agua")
elif(nivelAgua>=200 and nivelAgua<450):
    print("la reprasa esta ok")
elif(nivelAgua>=450):
    print("cuidado, abra compuertas")
else:
    print("digito un nivel invalido")

# Ejemplo 2 Estaciones

mes=input("Ingresar el mes que desea consultar: ").lower()

if(mes=='enero' or mes=='febrero' or mes=='marzo'):
    print("Actualmente nos encontramos en invierno")

elif(mes=='abril' or mes=='mayo' or mes=='junio'):
    print("Actualmente nos encontramos en verano :v")

elif(mes=='julio' or mes=='agosto' or mes=='septiembre'):
    print("Actualmete nos encontramos en Otoño :3")

elif(mes=='octubre' or mes=='noviembre' or mes=='diciembre'):
    print("Actualmente nos encontramos en primavera")

else:
    print("Error, ingresa un mes valido..")

'''

#ejemplo 3 edades:
'''edad=float(input("Digite la edad: "))
if(edad>=0 and edad<=14):
    print("la etapa de la vida en la que se encuentra es: NIÑO")
elif(edad>14 and edad<=28):
    print("la etapa de la vida en la que se encuentra es: JOVEN")
elif(edad>28 and edad<60):
    print("la etapa de la vida en la que se encuentra es: ADULTO")
elif(edad>=60):
    print("la etapa de la vida en la que se encuentra es: ADULTO MAYOR")
else:
    print("error al digitar la edad:")'''

#ejemplo 4 operador ternario
parametro=False

'''if(parametro==True):
    print("el parametro es verdadero")
else:
    print("El parametro es falso")'''

#Operador Ternario
print("el parametro es verdadero") if parametro==True else print("El parametro es falso")

estalloviendo=False
#if(estalloviendo==True):
    #print("esta lloviendo")
#else:
    #print("no esta lloviendo")    

print("esta lloviendo") if estalloviendo==True else  print("no esta lloviendo") 
