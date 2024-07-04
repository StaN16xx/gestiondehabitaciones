
estudiantes = []

def resgistrar_estudiante():
    nombre = input("ingrese el nombre de estudiante: ")
    rut = input("ingrese el rut de estudiante: ")
    nota1 = float(input("ingrese la nota 1:"))
    nota2= float(input("ingrese la nota 2:"))
    nota3 = float(input("ingrese la nota 3:"))
    nota4 = float(input("ingrese la nota 4:"))
    return Estudiante(rut, nombre, nota1,nota2,nota3,nota4)

def calcular_promedio(self):
    return sum(self.notas) / len(self.notas)

def listar_estudiantes():
    if not estudiantes:
        print("no hay estudiantes registrados")
    else:
        for estudiante in estudiantes:
            print(estudiantes.detalles_estudiante()) 

def menu_principal():
    while True:
        print("-----Menu----")
        print("1. Registrar estudiante:")
        print("3. Vizualisar estudiantes:")
        print("5. Salir del programa:")
        print("------------------------")

        opcion = input("seleccione una opcion:")
        if opcion == "1":
            resgistrar_estudiante()
        elif opcion == "3":
            listar_estudiantes()
        elif opcion == "5":
             print("Saliendo del programa")
             break
        else:
            print("opcion ivalida")
     

class Estudiantes:
    def _init_(self, nombre, rut, nota1, nota2, nota3, nota4):
        self.nombre = nombre
        self.rut = rut
        self.notas = [nota1,nota2,nota3,nota4]

if __name__ == "__main__":
    menu_principal()




