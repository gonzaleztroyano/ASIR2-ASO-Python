#!/usr/bin/python3


# Crea una clase Empleado que modele la información que una empresa mantiene sobre cada empleado: NIF, sueldo base, pago por hora extra, horas extra realizadas en el mes, tipo (porcentaje) de IRPF, casado o no y número de hijos. 
# Al crear un empleado se podrá proporcionar, si se quiere, el número de DNI. 
# Además los objetos deberán: 
#     • devolver el complemento correspondiente a las horas extra realizadas. 
#     • devolver el sueldo bruto. 
#     • devolver las retenciones (IRPF) a partir del tipo, teniendo en cuenta que el porcentaje de retención que hay que aplicar es el tipo menos 2 puntos si el empleado está casado y menos 1 punto por cada hijo que tenga; el porcentaje se aplica sobre todo el sueldo bruto. 
#     • print visualiza la información básica del empleado (sueldo base, complemento por horas extra, sueldo bruto, retención de IRPF y sueldo neto). 
#     • un método especial imprime_todo() muestra toda la información del empleado. 
#     • copia(): clona el objeto. 


class empleado():
    def __init__(self, nif, sueldo_base, horas_extra_pago, horas_extra_num, irpf_porcentaje, casado, hijos_no):
        self.nif = nif
        self.sueldo_base = sueldo_base
        self.horas_extra_pago = horas_extra_pago
        self.horas_extra_num = horas_extra_num
        self.irpf_porcentaje = irpf_porcentaje
        self.casado = casado
        self.hijos_no = hijos_no

    def horas_extras_debido(self):
        return self.horas_extra_pago * self.horas_extra_num

    def sueldo_bruto(self):
        return self.sueldo_base

    def retenciones_porcentaje(self):
        irpf_porcentaje_updated = self.irpf_porcentaje
        if self.hijos_no > 0:
            irpf_porcentaje_updated = self.irpf_porcentaje - ( self.hijos_no / 100)
        if self.casado == True:
            irpf_porcentaje_updated = irpf_porcentaje_updated - 0.02
        return irpf_porcentaje_updated 

    def retenciones_lereles(self):
        return -(self.sueldo_base * self.retenciones_porcentaje())

    def sueldo_neto(self):
        return  self.sueldo_base + self.retenciones_lereles() + self.horas_extras_debido()

    def imprime(self):
        print("Sueldo base del empleadx:    ", self.sueldo_base,"€")
        print("Complemento por horas extras:", self.horas_extras_debido(),"€/hora")
        print("Retención IRPF del empleadx: ", self.retenciones_lereles(),"€")
        print("Sueldo neto del empleadx:    ", self.sueldo_neto(),"€")
        print("   NOTA: Sueldo base + retenciones + horas extras")

    def imprime_todo(self):
        print("NIF:           ", self.nif)
        print("Sueldo base:   ", self.sueldo_base,"€")
        print("H.Extras - N:  ", self.horas_extra_num,"horas")
        print("H.Extras - €/N:", self.horas_extra_pago,"€/hora")
        print("H.Extras - €:  ", self.horas_extras_debido(),"€")
        print("IRPF - % base: ", (self.irpf_porcentaje * 100),"%")
        print("IRPF - --€:    ", self.retenciones_lereles(),"€")
        if self.casado:
            print("Casadx:         Sí, lo está.")
        else:
            print("Casadx:         No, no lo está.")
        if self.hijos_no > 0:
            print("Hijos/as:      ", self.hijos_no)
        else:
            print("Hijos/as:       NO tiene")
        print("")
        print("SUELDO NETO:   ",self.sueldo_neto(),"€")    
        
pepe = empleado("1A",1200,50,5,0.25,False,8)

pepe.imprime()
print("-------------")
pepe.imprime_todo()