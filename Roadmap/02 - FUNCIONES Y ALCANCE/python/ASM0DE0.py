# funciones simple

def greed():
    print("hola mundo")


greed()


#funciones con retorno

def return_greed():
    return("que pasa")

return_greed()

print(return_greed())

#funcion con argumentos determinado

def datos():
    return "asmodeo", 33 , "chile"

nombre, edad, pais = datos()

print("pais:" + pais)
print("edad: " + str(edad))
print("nombre:" + nombre)

print (datos)

#funciones dentro de funciones

que_dia_es_hoy = (input("que dia es hoy:"))


if que_dia_es_hoy == "lunes":
    print("que paja") 
    que_hora_es = int(input("que hora es :"))
    if que_hora_es == 11 :
        print("chupalo entonces")

if que_dia_es_hoy == "martes":
    print("meee")
    que_hora_es = int(input("que hora es :"))
    if que_hora_es == 13 :
        print("mas me crece")

if que_dia_es_hoy == "miercoles":
    print("ombligo")

if que_dia_es_hoy == "jueves":
    print("hoy se toma")

if que_dia_es_hoy == "viernes":
        print("hoy se toma tambien")

if que_dia_es_hoy == "sabado":
        print("hoy se hace asado")

if que_dia_es_hoy == "domingo":
    print("hoy leemos")

# funciion con un numero variable de argumentos

def variables_argumentos (*names):
    for name in names:
        print(f"dia: {name}")
        
variables_argumentos("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")

print(variables_argumentos)

# con numero bariable de aurgumentos y palabra calve

campeon = {
    "nombre": "briar" ,
    "linea" : "jungla",
    "rol" : "luchador",
    "1mer item" : "eclipse"
}

for campeon, detalle in campeon.items():
    print(campeon, "es:", detalle)
    
print()
print(" otro ejemplo")
print()

campeon = {
    "briar": ["jungla" , "luchador", "ecplipse"],
    "braum": ["soporte", "tanke" , "capa"] ,
    "jhin" : ["adc" , "carry" , "espadon"]
}


for nombre, (linea, rol, objeto) in campeon.items():
    print("nombre:" , nombre , "linea:" , linea, "rol:" ,rol , "objeto:" ,objeto )

print()
print("otro ejemplo")
print()

def saluda_5_campeones(*names):
    for name in names:
        print(f"\nhola, {name}!")
        
saluda_5_campeones("cait", "nautilus", "brand", "atrox", "rammus")

# funciones dentro de funciones

def funcion_externa():
    print("hola aa")
    def funcion_interna():
        print("hola bb")
    funcion_interna()
funcion_externa()


# funciones del lenguaje (build in )

print("\n1. print() -> mostrar texto")
print("Hola")


print("\n2. input() -> pedir datos")
nombre = input("Nombre: ")


print("\n3. len() -> contar elementos")
print(len("Python"))


print("\n4. type() -> mostrar tipo")
print(type(10))


print("\n5. int() -> convertir a entero")
print(int("5"))


print("\n6. float() -> convertir a decimal")
print(float("5.5"))


print("\n7. str() -> convertir a texto")
print(str(100))


print("\n8. bool() -> convertir a booleano")
print(bool(1))


print("\n9. list() -> convertir a lista")
print(list("abc"))


print("\n10. tuple() -> convertir a tupla")
print(tuple([1,2]))


print("\n11. set() -> crear conjunto")
print(set([1,1,2]))


print("\n12. dict() -> crear diccionario")
print(dict(nombre="Eduardo"))


print("\n13. max() -> valor máximo")
print(max(1,5,3))


print("\n14. min() -> valor mínimo")
print(min(1,5,3))


print("\n15. sum() -> sumar valores")
print(sum([1,2,3]))


print("\n16. abs() -> valor absoluto")
print(abs(-10))


print("\n17. round() -> redondear")
print(round(5.7))


print("\n18. range() -> rango de números")
print(list(range(5)))


print("\n19. sorted() -> ordenar")
print(sorted([3,1,2]))


print("\n20. enumerate() -> índice + valor")
for i, v in enumerate(["a","b"]):
    print(i, v)
    


# variante local y global 

glo_var = "casco azul"

def mamama():
    local_var = "casco verde"
    print(f"{local_var}")
    
mamama()
print(glo_var)

# print(local_var) # al estar aqui no sirbe
print()
# trabajo extra

def print_2_text(text_1,text_2)->int:
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0 :
            print(text_1)
        elif number % 5 == 0:
            print (text_2)
        else:
             print(number)
             count += 1
    return count

print(print_2_text("texto_1","text_2"))
