#model
class Ingreso():
    
    __entrada1 = ""
    __entrada2 = ""
    __entrada3 = ""
    __entrada4 = ""
    __regexLetras = "[a-zA-Z]"
    __regexOperadores = "[+-]"
    __regexDigitos = "\d*\.?\d*$"
    __regex2 = "^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$"
    __regex3 = "^[^@]+@[^@]+\.[a-zA-Z]{2,}$"
    __regexNotacion = "^[+-]?([0-9]*[.])?[0-9]+([eE][-+]?\d+)$"

    #Getters
    def getEntrada1(self):
        return self.__entrada1

    def getEntrada2(self):
        return self.__entrada2

    def getEntrada3(self):
        return self.__entrada3
        
    def getEntrada4(self):
        return self.__entrada4
        
    def getRegexLetras(self):
        return self.__regexLetras
    
    def getRegexOperadores(self):
        return self.__regexOperadores
    
    def getRegexDigitos(self):
        return self.__regexDigitos

    def getRegex2(self):
        return self.__regex2
    
    def getRegex3(self):
        return self.__regex3
    
    def getRegexNotacion(self):
        return self.__regexNotacion

    #Setters
    def setEntrada1(self, param):
        self.__entrada1 = param

    def setEntrada2(self, param):
        self.__entrada2 = param
    
    def setEntrada3(self, param):
        self.__entrada3 = param

    def setEntrada4(self, param):
        self.__entrada4 = param