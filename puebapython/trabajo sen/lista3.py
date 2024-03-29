def lista_unidad(estudiantes):
    listas_por_unidad = [[] for _ in range(5)]  
    
    for estudiante in estudiantes:
        unidad = int(estudiante)
        listas_por_unidad[unidad].append(estudiante)
    
    return listas_por_unidad



estudiantes = [2.5, 4.2, 1.8, 3.6, 2.1]

listas_por_unidad = lista_unidad(estudiantes)
for i, lista_unidad in enumerate(listas_por_unidad):
    print(f"Unidad {i + 1}: {lista_unidad}")