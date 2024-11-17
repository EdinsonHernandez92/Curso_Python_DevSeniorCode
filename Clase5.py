estudiantes = []
cursos = ['Java','Python']
docentes = []
horarios = []

# función para matricular un estudiante
def matricularEstudiante():
    nombre = input('Digite el nombre del estudiante: ')
    print('Seleccione el curso a matricular: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
    
    cursoSeleccionado = int(input('Ingrese el número del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        estudiante = {'nombre': nombre, 'curso': curso}
        estudiantes.append(estudiante)
        print(f'Estudiante: {nombre}, matriculado en el curso {curso}')
    else:
        print