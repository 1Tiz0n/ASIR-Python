##Listas TUPLAS Diccionarios
#ALT+SHIFT +E

#crea la alista de los dias de la semana y muestrame el primero y el último día de la semana.

days = [ "Lunes", "Martes", "Miercoles", "Jueves", "Viernes","Sabado", "Domingo"]
print("Primer día de la semana: ", days[0])
print("Ultimo dia de la semana: ", days[1])

#2. Modificar un elemento de una lista de frutas y añadir una nueva fruta al final

fruits = ["Apples", "Bananas", "kiwis"]
print( fruits)

fruits[0] = "Mango"
print(fruits)
fruits.append( "Melon")
print(fruits)

#3. Crea un aista vacia y llenala con 3 colores y llenalá con tres colores usando append()

colors = []
colors.append("Blue")
print(colors)
colors.append(['Red', 'Green'])
print(colors)

#4. Ordename una lista de numeros desordenados y muestrala al reves

numbers = [ 6,3,4,0,1,8,7,2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#5. ELimina un elemento de una lista y muestra el resultado

animals = ["Dog","Octopus", "Turtle","Cat","Parrot"]
print(animals)
animals.remove("Cat")
print(animals)

#6. Cuenatme cuantas veces aparece un numero en una lista de numeros

numeritos = [4,6,7,3,1,8,9,5,0,2,7,4,1]
quantity =numeritos.count(1)
print(quantity)
print("El número de veces que se repite el numero es: ", quantity)

#7. Crea una tupla con tres elementos de distinto tipo cada uno
mi_tupla = (19,"Gonzalo",True)
print("numero: ", mi_tupla[0])
print("numero: ", mi_tupla[1])
print("numero: ", mi_tupla[2])

#8. Acceder al segundo elemento de una tupla anidada dentro de una lista

List_data = ["Nombre", (100,200), "Apellidos"]
Tuple_mid = List_data[1]
print(Tuple_mid)

#9. Desempaquetar una tupla en 3 variables y muestramelas

Person = ("Sara", 43, "Malaga")
