#Controller
import re
from tkinter import *
class Validador:
    

    def validador_nombres(self, Ingreso):
        regex0 = re.compile(Ingreso.getRegex1())
        print(f"regex: {regex0}")
        cadena0 = (Ingreso.getEntrada1()) 
        print(f"cadena: {cadena0}")
        Ingreso.setEntrada1("")
        resultado = regex0.match(cadena0)
        if bool(resultado) == True:
            return True
        else:
            return False
    
    def validador_numeros(self, Ingreso):
        regex1 = re.compile(Ingreso.getRegex2())
        print(f"regex: {regex1}")
        cadena1 = Ingreso.getEntrada2()
        print(f"cadena: {cadena1}")
        Ingreso.setEntrada2("")
        resultado = regex1.match(cadena1)
        if bool(resultado) == True:
            return True
        else:
            return False
            
    def validador_correos(self, Ingreso):
        regex2 = re.compile(Ingreso.getRegex3())
        print(f"regex: {regex2}")
        cadena2 = Ingreso.getEntrada3()
        print(f"cadena: {cadena2}")
        Ingreso.setEntrada3("")
        resultado = regex2.match(cadena2)
        if bool(resultado) == True:
            return True
        else:
            return False

    def validador_notacion(self, Ingreso):
        regex4 = re.compile(Ingreso.getRegex4())
        print(f"regex: {regex4}")
        cadena4 = Ingreso.getEntrada4()
        print(f"cadena: {cadena4}")
        Ingreso.setEntrada4("")
        resultado = regex4.match(cadena4)
        if bool(resultado) == True:
            return True
        else:
            return False  