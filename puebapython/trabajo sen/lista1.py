def lista_reprobados(estudiantes):
    aprobados = []
    reprobados = []
    
    for estudiante in estudiantes:
        if estudiante['calificacion'] >= 3:
            aprobados.append(estudiante)
        else:
            reprobados.append(estudiante)
    
    return aprobados, reprobados


def lista_unidad(estudiantes):
    listas_por_clase = [[] for _ in range(5)] 
    
    for estudiante in estudiantes:
        clase = int(estudiante['calificacion'])
        listas_por_clase[clase].append(estudiante)
    
    return listas_por_unidad


def calcular_promedio(estudiantes):
    if len(estudiantes) == 0:
        return 0
    
    total = sum(estudiante['calificacion'] for estudiante in estudiantes)
    promedio = total / len(estudiantes)
    return promedio


estudiantes = [
    {'nombre': 'Estudiante1', 'calificacion': 2.5},
    {'nombre': 'Estudiante2', 'calificacion': 4.2},
    {'nombre': 'Estudiante3', 'calificacion': 1.8},
    {'nombre': 'Estudiante4', 'calificacion': 3.6},
    {'nombre': 'Estudiante5', 'calificacion': 2.1},
]

aprobados, reprobados = lista_reprobados(estudiantes)
print("Aprobados:")
for estudiante in aprobados:
    print(estudiante['nombre'])
print("Reprobados:")
for estudiante in reprobados:
    print(estudiante['nombre'])


listas_por_unidad = lista_unidad(estudiantes)
for i, lista_unidad in enumerate(listas_por_unidad):
    print(f"salon {i + 1}:")
    for estudiante in lista_unidad:
        print(estudiante['nombre'])

promedio_aprobados = calcular_promedio(aprobados)
promedio_reprobados = calcular_promedio(reprobados)
print(f"Promedio de aprobados: {promedio_aprobados}")
print(f"Promedio de reprobados: {promedio_reprobados}")


