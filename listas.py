#listas
lista=[]
print(lista)

#lista semana
listasemana=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print(listasemana[0])

#lista semana
listasemana=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print(listasemana[-1])


#lista semana
listasemana=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print(listasemana[0,3])

#quitar los elementos repetidos de una lista
listaa=[1,2,3,4,"hola",2,2]
conjunto=set(listaa)
listaa=listaa(conjunto)
print(conjunto)

#listas palabras de 2 listas
lista1palabras=["Sofia","Karla","Verinica","Lina","Natalia","Estefania"]
lista2palabras=["Enrique","Erica","Sofia","Lina","Carlos","Pablo"]
print(lista1palabras,lista2palabras)

#listas de palabras que aparecen en la primera lista
lista1palabras=["Sofia","Karla","Verinica","Lina","Natalia","Estefania"]
lista2palabras=["Enrique","Erica","Sofia","Lina","Carlos","Pablo"]
print(lista1palabras[1,2,4,5],lista2palabras)

#listas de palabras que aparecen en la segunda lista
lista1palabras=["Sofia","Karla","Verinica","Lina","Natalia","Estefania"]
lista2palabras=["Enrique","Erica","Sofia","Lina","Carlos","Pablo"]
print(lista2palabras[0,1,4,5],lista1palabras)


#listas palabras repetidas en ambas listas
lista1palabras=["Sofia","Karla","Verinica","Lina","Natalia","Estefania"]
lista2palabras=["Enrique","Erica","Sofia","Lina","Carlos","Pablo"]
print(lista1palabras,lista2palabras[0,3])
