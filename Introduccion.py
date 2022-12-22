print("hello word") #comentarios
varEntera = 1
varDecimal = 1.2
varCadena1 = "hola"
varCadena2 = "mundo"
varBooleana = False

print(type(varEntera))
print(type(varDecimal))
print(type(varCadena1))
print(type(varBooleana))

SumaNumeros = varEntera + varDecimal
print(SumaNumeros)
SumaCadenas = varCadena1 + varCadena2
print(SumaCadenas)

#para convertir directamente le ponemos int, float, str, etc

#help y lo que queremos saber
#help(type)


#estructuras de datos
#vectores, listas
lista1=["hola", 1, 1.0]
print(lista1)
print(lista1[0])  #imprimimos el primer elemento
#tuplas: no  se pueden modificar
tupla1= "chau", 1, 3.9
tupla2= ("hola", 7, 9)
print(tupla1)
print(tupla1[0]) 
print(tupla2)
print(tupla2[0]) 
#diccionarios, almacenan informacion, son como json
diccionario1 = { "NOMBRE": "Juan",
  "APELLIDO": "Perez", 
  "EDAD": "2"}
print(diccionario1)  
diccionario1["ALTURA"]="1metro" #sumamos un elemento mas
print(diccionario1)  
#set, no guardan elementos repetidos, ni se buscan por subindices
# set of integers
my_set = {1, 2, 3}
print(my_set)
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)


#estructuras condicionales
#if, elif, else
a=2
b=1
if (a<b):   
  print("a es menor que b")
elif (a==b):
  print("a y b son iguales")
else:
  print("a es mayor que b")
#for
for letra in "texto":
  print(letra)
listaFor=["hola", "hola1", "hola2"]
for elementos in listaFor:
  print(elementos)
for elementosRango in range(20):
  print(elementosRango)
for elementosRango in range(5,15):
  print(elementosRango)
for indiceLista in range(len(listaFor)):
  print("indice de la lista", indiceLista)
  print("elemento de la lista", listaFor[indiceLista])
#while
i=1
while (i<=4):
  print(i)
  i=i+1
