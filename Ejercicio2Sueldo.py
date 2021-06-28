class sueldo:
    def __init__(self):
        pass
    
    def operarSueldo(self):
        
        sb=float(input("Ingrese sueldo base:"))
        v1=float(input( "ingrese valor 1:"))
        v2=float(input("ingrese valor 2:"))
        v3=float(input("ingrese valor 3:"))
        tv=v1+v2+v3
        com=tv*(10/100)
        tr=sb+com
        print("El sueldo total a recibir es:", tr)

op1=sueldo()
op1.operarSueldo()        

