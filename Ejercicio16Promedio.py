class promedio:
    def __init__(self):
        pass

    def calificacion(self):
        i=1
        j=1
        for i in range(1,30):
            for j in range(1,6):
                print("escriba la calificacion del alumno", i, "en el examen", j)
                calificaciones =float(input([i,j]))
    
    def promedioCalificaciones(self):
        calificaciones =float(input[i,j])
        j=1
        for j in range(1,6):
            sum=0
            i=1
            for i in range(1,30):
                sum=sum+calificaciones 
                prom=sum/30
                print("promedio examen", j ,prom )    

    def promedioAlumno(self):
        i=1
        for i in range(1,30):
            calificaciones =float(input[i,j])
            sum1=0 
            j=1
            for j in range(1,6):
                sum1=sum1+calificaciones
                print("promedio del alumno", i, sum1/6)

    # #def promedioExamen(self,prom=1):
    #     examen=1
    #     proMayor=prom
    #     j=2
    #     for j in range(2,6):
    #         if proMayor< 

prome1=promedio()
prome1.calificacion()
prome1.promedioCalificaciones()
prome1.promedioAlumno()    




