def porcentaje(nota):
    if nota >= 9:
        return "Excelente"
    elif nota > 5:
        return "Bien"
    elif nota == 5:
        return "Suficiente"
    elif nota < 5:
        return "Insuficiente"
    else:
        return "Muy insuficiente"

try:
    nota = float(input("Ingrese la nota (0-10): "))

    if 0 <= nota <= 10:
        calificacion = porcentaje(nota)
        print(f"La calificación es: {calificacion}")
    else:
        print("La nota ingresada está fuera del rango permitido.")
except ValueError:
    print("Por favor, ingrese solo números válidos.")