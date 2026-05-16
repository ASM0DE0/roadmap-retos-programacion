# operadores y estructuras

#operaciones
#la f y despues del = al usar {} se usa la programacion de la operacion
print (f"suma: 10 + 3 = {10 + 3}")
print (f"resta: 10 - 3 = {10 - 3}")
print (f"division: 10 / 3 = {10 / 3}")

#modulo se hace con el % y es lo que sobra en una division de fracciones
print (f"modulo: 10 % 3 = {10 % 3}")
print (f"modulo: 16 % 3 = {16 % 3}")

print (f"exponente: 10 ** 3 = {10 ** 3}")

print (f"division entera: 10 // 3 = {10 // 3}")

#operadores de comparacion

# el operador de igualdad igual se puede udar para comparar cadenas de texto
print (f"igualdad: 10 == 3 = {10 == 3}")

#desigualdad
print (f"desigualdad: 10 != 3 = {10 != 3}")

#mayor que y menor que
print (f"mayor que: 10 > 3 = {10 > 3}")
print (f"menor que: 10 < 3 = {10 < 3}")

#mayor o igual que y menor o igual que
print (f"mayor o igual que: 10 >= 3 = {10 >= 3}")
print (f"menor o igual que: 10 <= 3 = {10 <= 3}")

#operadores logicos

# operador AND es para verficar que ambos sean verdaderas para que salga una opcion vinaria que sera v o f
print (f"AND : 10 + 5 == 15 and 6 - 2 == 4 {10 + 5 == 15 and 6 - 2 == 4}")

# el or solorequerira que una sea verdadera para que slaga verdadera
print (f"or : 10 + 5 == 15 or 6 - 2 == 5 {10 + 5 == 15 or 6 - 2 == 5}")

# operador not sirve para invertir un booleano
print (f"not : not 10 + 5 == 15 {not 10 + 5 == 15 }")

#operador de asisgnacion

my_number = 10   #asignacion
print(my_number)
print(my_number)
my_number += 4  #suma y asignacion
print(my_number)
my_number -= 7  #sresta y asignacion
print(my_number)
my_number *= 2  #sresta y asignacion
print(my_number)
my_number /= 1  #fivision y asignacion
print(my_number)
my_number %= 8  #modulo y asignacion
print(my_number)
my_number **= 3  #exponente y asignacion
print(my_number)
my_number //= 4  #division entera y asignacion
print(my_number)

'''operador de identidad , ve mas que el valor , la posicion
donde esta la palabra o numero y es con un "is" '''

#operador de identidad
my_number_a = (54)
print(f"my_number_a is my_number {my_number_a is my_number}")

#operador de not identidad

print(f"my_number_a is not my_number {my_number_a is not my_number}")

#operadores de pertenecia ( son para ver si algo esta en una lista)

print(f"la letra 't' este en caballo = {'t' in 'caballo'}")

print(f"la letra 'c' este en caballo = {'c' in 'caballo'}")

#operadores de bit

# OPERADOR AND (&)
# ambos tienen que ser 1 o verdadero para que den 1

a = 4
b = 8


resultado = a & b

print("a =", a, "=" , bin(a))
print("b =", b, "=" , bin(b))
print("resultado =" , resultado , "=" , bin(resultado))

#  OPERADOR OR (|)
# basta conque 1 de los dos sea verdadero o 1 para que sea verdadero

print()

a = 4
b = 8


resultado = a | b

print("a =", a, "=" , bin(a))
print("b =", b, "=" , bin(b))
print("resultado =" , resultado , "=" , bin(resultado))


# operador xor (^) , solo da 1 si los bit son distintos

print()

a = 3
b = 8


resultado = a ^ b

print("a =", a, "=" , bin(a))
print("b =", b, "=" , bin(b))
print("resultado =" , resultado , "=" , bin(resultado))


# OPERADOR NOT (~) inbierte los bits

#PYTHON USA:
# COMPLEMENTO A DOS
# POR ESO EL RESULTADO ES NEGATIVO
print()

a = 9

resultado = ~a 

print("a =", a, "=" , bin(a))
print("resultado =" , resultado , "=" , bin(resultado))

# SHIFT IZQUIERDA (<<) mueve los bits 1 espacio a la izquierda
#lo que lo multiplica por 2

print()

a = 9

resultado = a << 1

print("a =", a, "=" , bin(a))
print("resultado =" , resultado , "=" , bin(resultado))

# SHIFT DERECHA (>>) mueve los bits 1 espacio a la derecha
#lo que lo divide por 2

print()

a = 10

resultado = a >> 1

print("a =", a, "=" , bin(a))
print("resultado =" , resultado , "=" , bin(resultado))

# ESTRUCTURAS DE CONTROL

# if es para ejecutar solo si se cumple la condicion 
print()

respuesta = input("que dia es hoy:")

if respuesta == "lunes" :
    print("que paja")
elif respuesta == "sabado" :
    print("wena")
elif respuesta == "domingo" :
    print("wena")
else:
    print("meeee")
    

#  for

for i in range(3,16):
    print(i)

# while

print()
i = 0

while i <= 9 :
    print(i)
    i += 1
    

# manejo de exepsiones 

# "try " 

try:
    print(10/0)
except:
    print("se ha producido un error")
finally:
    print("se a finalizado el manejo de error")


# brake es para que rompa el ciclo de inmediato, la palabra o el numero del brake no sera mostrado

for numero in range(1, 11):

    if numero == 5:
        break

    print(numero)
    

# continue es para que salte el numero o palabra mencionado y siga con el resto

for numero in range(1, 6):

    if numero == 3:
        continue

    print(numero)
    

# pass no hace nada en la cuenta mas que dejar una marca

for numero in range(5):

    if numero == 3:
        pass

    print(numero)
    

# match , es como para dar opciones a una condicional

dia = 3

match dia:

    case 1:
        print("Lunes")

    case 2:
        print("Martes")

    case 3:
        print("Miercoles")

    case _:
        print("Dia no valido")
        

# ejercicio

for numero in range(10, 56):
    if numero % 2 == 1:
        continue
    if numero % 3 == 0:
        continue
    if numero == 16:
        continue
    print(numero)
    
    

