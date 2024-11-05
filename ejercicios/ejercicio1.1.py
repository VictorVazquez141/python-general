
#Duración de los cursos 
cursos_min = 2.5
cursos_max = 7
cursos_promedio = 4
curso_actual = 1.5

#Diferenencias de duración X video 
duracion_min = 100 - (curso_actual / cursos_min * 100)
duracion_max = 100 - (curso_actual*1000 // cursos_max /10)
duracion_promedio = 100 - (curso_actual / cursos_promedio * 100)

print(f"El curso actual dura {duracion_min}% menos que el mas rapido")
print(f"El curso actual dura {duracion_max}% menos que el mas lento")
print(f"El curso actual dura {duracion_promedio}% menos que el mas promedio")
