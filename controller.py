# Controller
import re


class Validador:

    def validador_nombres(self, Ingreso):
        regex0 = re.compile(Ingreso.getRegexLetras())
        cadena0 = (Ingreso.getEntrada1())
        Ingreso.setEntrada1("")
        returns = ["", True]
        for caracter in cadena0:
            validar = regex0.match(caracter)
            if validar == True:
                returns[0] = ""
                returns[1] = bool(validar)
            else:
                returns[1] = bool(validar)
                returns[0] = caracter
                if False == returns[1]:
                    break
        return returns

    def validador_numeros(self, Ingreso):
        regexOperadores = re.compile(Ingreso.getRegexOperadores())
        regexDigitos = re.compile(Ingreso.getRegexDigitos())
        cadena1 = Ingreso.getEntrada2()
        Ingreso.setEntrada2("")
        returns = ["", True]
        validarOperadores = bool(regexOperadores.match(cadena1[0]))
        if bool(validarOperadores) == True:
            returns[0] = ""
            returns[1] = bool(validarOperadores)
            for caracter in cadena1[1:]:
                validarDigitos = bool(regexDigitos.match(caracter))
                if (bool(validarOperadores) == True and returns[1] == False):
                    returns[1] = bool(validarDigitos)
                    returns[0] = ""
                else:
                    returns[1] = bool(validarDigitos)
                    returns[0] = caracter
                    if False == returns[1]:
                        break
            return returns
        else:
            returns[1] = bool(validarOperadores)
            returns[0] = cadena1[0]
            return returns

    def validador_correos(self, Ingreso):
        regexLetras = re.compile(Ingreso.getRegexLetras())
        regexDigitos = re.compile(Ingreso.getRegexDigitos())
        cadena2 = Ingreso.getEntrada3()
        Ingreso.setEntrada3("")
        returns = ["", True]
        for caracteres in cadena2:
            validar = bool(regexLetras.match(caracteres))
            if (bool(validar) == True or bool(regexDigitos.match(caracteres)) == True and "@" in cadena2):
                returns[0] = ""
                returns[1] = True
            elif (caracteres == "-" or caracteres == "_" or caracteres == "." and "@" in cadena2):
                returns[0] = ""
                returns[1] = True
            elif (caracteres == "@"):
                try:
                    cadena_dividida = cadena2.split('@')
                    validar = bool(regexLetras.match(cadena_dividida[1]))
                    if (bool(validar) == True):
                        returns[0] = ""
                        returns[1] = True
                except:
                    returns[1] = False
                    break
            else:
                returns[0] = "Error causado debido a que no es un correo electronico ya que no cuenta con un @ o debido al caracter: ", caracteres
                returns[1] = False
                break

        return returns

    def validador_notacion(self, Ingreso):
        regexOperadores = re.compile(Ingreso.getRegexOperadores())
        regexDigitos = re.compile(Ingreso.getRegexDigitos())
        regexNotacion = re.compile(Ingreso.getRegexNotacion())
        cadena4 = Ingreso.getEntrada4()
        Ingreso.setEntrada4("")
        returns = ["", True]
        validarOperadores = bool(regexOperadores.match(cadena4[0]))
        print(validarOperadores)
        if bool(validarOperadores) == True:
            returns[0] = ""
            returns[1] = bool(validarOperadores)
            for caracter in cadena4[1:]:
                validarDigitos = bool(regexDigitos.match(caracter))
                if (bool(validarDigitos) == True and returns[1] == False):
                    returns[1] = bool(validarDigitos)
                    returns[0] = ""
                elif ("e" in caracter or "E" in caracter):
                    returns[1] = bool(validarDigitos)
                    returns[0] = ""
                else:
                    returns[1] = bool(validarDigitos)
                    returns[0] = caracter
                    if False == returns[1]:
                        break
            return returns
        else:
            returns[1] = bool(validarOperadores)
            returns[0] = cadena4[0]
            return returns
