class aumento:
    def __init__(self):
        pass

    def calcularSalario(self):
        
        sueldo=float(input("Ingrese sueldo inicial: "))
        if sueldo <= 600:
            SF=sueldo+(sueldo*0.1)
        else:
            SF=sueldo
        print("Su sueldo actual es de:", SF) 

suel1=aumento()
suel1.calcularSalario()                