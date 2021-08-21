#model
class Ingreso():
    
    __entrada1 = ""
    __entrada2 = ""
    __entrada3 = ""
    __regex1 = "[a-zA-Z]"
    __regex2 = "^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$"
    __regex3 = "^[^@]+@[^@]+\.[a-zA-Z]{2,}$"

    #Getters
    def getEntrada1(self):
        return self.__entrada1

    def getEntrada2(self):
        return self.__entrada2

    def getEntrada3(self):
        return self.__entrada3
        
    def getRegex1(self):
        return self.__regex1

    def getRegex2(self):
        return self.__regex2
    
    def getRegex3(self):
        return self.__regex3

    #Setters
    def setEntrada1(self, param):
        self.__entrada1 = param

    def setEntrada2(self, param):
        self.__entrada2 = param
    
    def setEntrada3(self, param):
        self.__entrada3 = param

