class calificacion:
    def __init__(self):
        pass

    def calcularCalificacion(self):
        nota=float(input("Ingrese nota: "))
        if nota >= 7:
            print("Aprobado")
        print("Fin del programa")

cal1=calificacion()
cal1.calcularCalificacion()            
