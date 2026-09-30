# Prolog

Ultima actualización: 2026-09-28

## EXAMPLE 1

alumno(x)<br>
profesor(x)<br>
carrera(x)<br>
materia(x)<br>
estudia_pred(x, y)<br>
cursa_pred(x, y)<br>
imparte_pred(x, y)

## EXAMPLE 2

Cinco consultas que se generan positivamente.

alumno_en_carrera(a, c)<br>
profesor_en_materia(p, m)<br>
alumno_en_materia(a, m)<br>
profesor_de_alumno(p, a)<br>
alumno_de_profesor(a, p)
