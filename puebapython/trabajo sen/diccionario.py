import random
def key(diccionario, clave):
    if clave in diccionario:
        solucion=diccionario[clave]
        return solucion
    else:
        return "La clave no existe en el diccionario"
diccionario_key={'libro':'palabras','pelicula':'actor','juguete':'niño'}

solucion = key(diccionario_key, str(input('escribe una palabra: ')))
print('resultado: ',solucion)
solucion = key(diccionario_key, str(input('escribe una palabra: ')))
print('resultado: ',solucion)

def animales(español,nal):
    if nal in español:
        nativo=español[nal]
        return nativo
    else:
        return "La clave no se traduce"
def contr(ingles,pal):
    if pal in ingles:
        traduccion=ingles[pal]
        return traduccion
    else:
        return "La clave no se encuentra"
animales_ingles1={'perro':'dog','gato':'cat','leon':'lion','tiburon':'shark'}
solucion = animales(animales_ingles1,'perro')
print('resultado: ',solucion)
solucion = animales(animales_ingles1,'gato')
print('resultado: ',solucion)
solucion = animales(animales_ingles1,'leon')
print('resultado: ',solucion)
solucion = animales(animales_ingles1,'tiburon')
print('resultado: ',solucion)

