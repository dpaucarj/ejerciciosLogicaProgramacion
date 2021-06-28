class bucleRepeat:
    def __init__(self):
        pass

    def leerNumero(self):
        serie=0
        I=1
        num=int(input("ingrese numero:"))
        band=True
        while True:
            if band is True:
                serie=serie+(1/I)
                band=False
            else:
                serie=serie-(1/I)
                band=True
            I=I+1
            print(serie)     

rep1=bucleRepeat()
rep1.leerNumero()           

        
