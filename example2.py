# PROLOG PREDICATES, EXAMPLE 2

alumnos = {"ana", "pepe", "sancho"}
profesores = {"profe_mario", "profe_oscar", "profe_sara"}
carreras = {"ing_sistemas", "ing_mecatronica", "ing_electronica"}
materias = {"calculo", "programacion", "quimica"}

estudia = {
    ("ana", "ing_sistemas"),
    ("pepe", "ing_mecatronica"),
    ("sancho", "ing_electronica"),
}

cursa = {
    ("ana", "programacion"),
    ("pepe", "calculo"),
    ("sancho", "quimica"),
}

imparte = {
    ("profe_mario", "programacion"),
    ("profe_oscar", "calculo"),
    ("profe_sara", "quimica"),
}

def alumno(x):
    return x in alumnos

def profesor(x):
    return x in profesores

def carrera(x):
    return x in carreras

def materia(x):
    return x in materias

def estudia_pred(x, y):
    return (x, y) in estudia

def cursa_pred(x, y):
    return (x, y) in cursa

def imparte_pred(x, y):
    return (x, y) in imparte

def alumno_en_carrera(a, c):
    return alumno(a) and carrera(c) and estudia_pred(a, c)

def profesor_en_materia(p, m):
    return profesor(p) and materia(m) and imparte_pred(p, m)

def alumno_en_materia(a, m):
    return alumno(a) and materia(m) and cursa_pred(a, m)

def profesor_de_alumno(p, a):
    if not (profesor(p) and alumno(a)):
        return False
    for m in materias:
        if imparte_pred(p, m) and cursa_pred(a, m):
            return True
    return False

def alumno_de_profesor(a, p):
    if not (alumno(a) and profesor(p)):
        return False
    for m in materias:
        if cursa_pred(a, m) and imparte_pred(p, m):
            return True
    return False

def ejecutar_consultas():
    pruebas = [
        ("alumno_en_carrera(ana, ing_sistemas)", alumno_en_carrera("ana", "ing_sistemas"), True),
        ("profesor_en_materia(profe_mario, programacion)", profesor_en_materia("profe_mario", "programacion"), True),
        ("alumno_en_materia(pepe, calculo)", alumno_en_materia("pepe", "calculo"), True),
        ("profesor_de_alumno(profe_oscar, pepe)", profesor_de_alumno("profe_oscar", "pepe"), True),
        ("alumno_de_profesor(sancho, profe_sara)", alumno_de_profesor("sancho", "profe_sara"), True),
    ]

    for consulta, resultado, esperado in pruebas:
        estado = "OK" if resultado == esperado else "MAL"
        print(f"?- {consulta}")
        print(f"   Resultado: {resultado} [{estado}]")
        print()

if __name__ == "__main__":
    ejecutar_consultas()