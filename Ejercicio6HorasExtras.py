# class trabajador:
#     def __init__(self):
#         pass

#     def determinarSalario(self):
#         ht=float(input("Ingrese horas trabajadas: "))
#         ph=float(input("Ingrese pago por hora normal: "))
#         if ht>40:
#             he=ht-40
#             if he>8:
#               het=he-8
#               phe=ph*2*8+ph*3*het
#             else:
#               phe=ph*2*he
#             pt=ph*40+phe
#         else:
#             pt=ph*ht
#         print("El pago total de horas trabajadas es :", pt)         

# det1=trabajador()
# det1.determinarSalario()         



class Tarea:

    def __init__(self):
      pass

    def pagoJornadaExtra(self):
      horas_trabajadas, horas_extras, horas_extras_triple=0,0,0
      valor_hora, pago_horas_extras, pago_total=0,0,0
      horas_trabajadas=int(input("ingrese horas trabajadas:") )
      valor_hora=float(input("ingrese valor hora:"))
      if(horas_trabajadas>40):
        horas_extras=horas_trabajadas-40
        if (horas_extras>8):
          horas_extras_triple=horas_extras-8
          pago_horas_extras=valor_hora*2*8+valor_hora*3*horas_extras_triple

        else:
          pago_horas_extras=valor_hora*2*horas_extras
        pago_total=valor_hora*40+pago_horas_extras
        
      else:
        pago_total=valor_hora*horas_trabajadas

      print("""horas trabajadas:{} horas extras:{} horas triple: {} valor hora:{}
       pago valor extra:{} pago total:{}""".format(horas_trabajadas,horas_extras,horas_extras_triple,valor_hora,pago_horas_extras,pago_total))  
        

pago=Tarea()
pago.pagoJornadaExtra()



