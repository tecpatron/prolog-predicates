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

pertenece = {
    ("ana", "ing_sistemas"),
    ("pepe", "ing_mecatronica"),
    ("sancho", "ing_electronica"),
}

inscrito = {
    ("ana", "programacion"),
    ("pepe", "calculo"),
    ("sancho", "quimica"),
}

asiste = {
    ("ana", "programacion"),
    ("pepe", "calculo"),
    ("sancho", "quimica"),
}

ensena = {
    ("profe_mario", "programacion"),
    ("profe_oscar", "calculo"),
    ("profe_sara", "quimica"),
}

requiere = {
    ("programacion", "calculo"),
    ("quimica", "calculo"),
}

especialista = {
    ("profe_mario", "programacion"),
    ("profe_oscar", "calculo"),
    ("profe_sara", "quimica"),
}

profesor_de = {
    ("profe_mario", "ing_sistemas"),
    ("profe_oscar", "ing_mecatronica"),
    ("profe_sara", "ing_electronica"),
}

alumno_de = {
    ("ana", "ing_sistemas"),
    ("pepe", "ing_mecatronica"),
    ("sancho", "ing_electronica"),
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

def ejecutar_consultas():
    pruebas = [
        ("alumno(ana)",              alumno("ana"),              True),
        ("alumno(profe_mario)",      alumno("profe_mario"),      False),

        ("profesor(profe_mario)",    profesor("profe_mario"),    True),
        ("profesor(ana)",            profesor("ana"),            False),

        ("carrera(ing_sistemas)",    carrera("ing_sistemas"),    True),
        ("carrera(calculo)",         carrera("calculo"),         False),

        ("materia(programacion)",    materia("programacion"),    True),
        ("materia(pepe)",            materia("pepe"),            False),

        ("estudia(ana, ing_sistemas)",   estudia_pred("ana", "ing_sistemas"),   True),
        ("estudia(ana, ing_mecatronica)", estudia_pred("ana", "ing_mecatronica"), False),

        ("cursa(pepe, calculo)",     cursa_pred("pepe", "calculo"),     True),
        ("cursa(pepe, quimica)",     cursa_pred("pepe", "quimica"),     False),

        ("imparte(profe_mario, programacion)", imparte_pred("profe_mario", "programacion"), True),
        ("imparte(profe_mario, quimica)",      imparte_pred("profe_mario", "quimica"),      False),
    ]

    for consulta, resultado, esperado in pruebas:
        estado = "OK" if resultado == esperado else "MAL"
        print(f"?- {consulta}")
        print(f"   Resultado: {resultado}  (esperado: {esperado})  [{estado}]")
        print()

if __name__ == "__main__":
    ejecutar_consultas()