
print("===============lista========================")

list = ["aa", "bb", "cc", "dd", 67, 3.14 , "ff"]

print(list)
print(type(list))  #tipo de 

list.append("zz")  # agregar
print(list)

list.remove("bb")  #sustraer
print(list)

print(list[4]) #imprimiir solo 1

list[1]= "hh"  #actualizar

print(list)

list = [str(x) for x in list]  # convertir numeros a texto

list.sort()

print(list)

print()
print("======================tuplas===========================") 

tupla_aa = (3.14, 2.71, "a^2+b^2=c^", "fibonacci")
print(tupla_aa)
print(tupla_aa[0]) #imprimiir solo 1#imprimiir solo 1

print(type(tupla_aa))
tupla_aa = [str(x) for x in tupla_aa] 
print(type(tupla_aa))

tupla_aa = tuple(sorted(tupla_aa))
print(tupla_aa) 

print(type(tupla_aa))
 
 
 
print("====================set====================")
#los set son desordanados

set = {"anillo de doran", "espada de doran", "escudo", "lagrima"}

print(set)

set.add("botas")

print(set)

set.add("botas") #no acepta duplicados

print(set)

# print(set[0]) no se puede imprimir por ubicacion porque estan desordenadas

set.remove("anillo de doran")

print(set) # si se puede remover

# el .sorted debolvera una lista

print("===============diccionaario==================")

# se hace con {} y debe llevar valor, detalle, siempre en pareja y separado por un :

dicc = {
    "zona" : "blue" ,
    "campeon" : "kayn",
    "linea" : "jg",
    "rol": "asesino"
}

print(dicc)
print(type(dicc))

print(dicc["linea"]) # nose puede acceder al dato pero si a la palabra calve
#print(dicc["jg"])  # pero no se puede al revez

dicc["linea"] = "top" #actualizacion

print(dicc)

del dicc["campeon"] # eliminacion

print(dicc)

#dicc = sorted(dicc.items()) #lo ordena pero convierte a lista
print(type(dicc))

dicc = dict(sorted(dicc.items()))  # lo ordena sin cambiarlo a lista

print(dicc)
print(type(dicc))

print("=================ejercicio===================")


def contactos():
    
    agenda = {}
    
    while True :
    
        print("\n1.- buscar contacto") 
        print("\n2.- insertar contacto") 
        print("\n3.- actualizar contacto") 
        print("\n4.- eliminar contacto") 
        print("\n5.- exit") 

        options = input("\nselecciona una opcion: ")

        match options:
            case "1":
                name = input("esccribe el nombre a buscar:")
                if name in agenda:
                    print(f"el numero de {name} es: {agenda[name]}.")                   
                else :
                    print("no encontrado.")                               
            case "2":
                name = input("esccribe el nombre:")
                phone = input("escribe el numero:")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone      
                else:
                    print("debe ser de menos de 12 digitos")          
            case "3":
                name = input("esccribe el nombre a actualizar:")
                if name in agenda:
                    phone = input("escribe el numero:")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone                
                else :
                    print("no encontrado.")                     
            case "4":
                name = input("esccribe el nombre a eliminar:")
                if name in agenda:
                    del agenda [name]
                else :
                    print("no encontrado.")              
            case "5":
                print("cerrando programa")
                break
            case _:
                print("elige una opcion del 1 al 5")
                
contactos()

