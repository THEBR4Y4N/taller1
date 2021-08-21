from tkinter import *
import model as m
import  controller as c

model = m.Ingreso()
controller = c.Validador()

root = Tk()
root.title('PROYECTO DE I-CORTE')
root.geometry("800x600")

# funcion1
def clic():
    Str()
    Int()
    Mail()

def Str():
        ingresado = str(e.get())
        model.setEntrada1(ingresado)
        validador = controller.validador_nombres(model)
        if bool(validador) == True:
            answer.config(text="Nombre escrito de manera correcta")
        else:
            answer.config(text="Nombre ha sido escrito de forma incorrecto")     


def Int():
        ingresado = str(e2.get())
        model.setEntrada2(ingresado)
        validador = controller.validador_numeros(model)
        if bool(validador) == True:
            answer2.config(text="El dato que ha ingresado en el campo es un número.")
        else:
            answer2.config(text="El dato que ha ingresado en el campo no corresponde a un número.")

def Mail():
        ingresado = str(e3.get())
        model.setEntrada3(ingresado)
        validador = controller.validador_correos(model)
        if bool(validador) == True:
            answer3.config(text="El campo corresponde a un correo electronico.")
        else:
            answer3.config(text="El campo NO corresponde a un correo electronico.")    


# Titulo_Principal
my_label1 = Label(root, text="Validador de expresiones regulares",
                 font=("Helvetica", 20))
my_label1.pack(pady=20)

# Titulo_1
my_label2 = Label(root, text="Cadena de Caracteres",
                 font=("Helvetica", 10))
my_label2.pack(pady=20)


# campo1
e = Entry(root, width=40, font=("Arial", 10))
e.pack()

# Titulo_2
my_label3 = Label(root, text="Números",
                 font=("Helvetica", 10))
my_label3.pack(pady=20)

# campo2
e2 = Entry(root, width=40, font=("Arial", 10),)
e2.pack()

# Titulo_3
my_label4 = Label(root, text="Correo Electronico",
                 font=("Helvetica", 10))
my_label4.pack(pady=20)

# campo3
e3 = Entry(root, width=40, font=("Arial", 10),)
e3.pack()

#response
answer= Label(root, text="", font=("Helvetica", 10))
answer.pack(pady=20)
answer2= Label(root, text="", font=("Helvetica", 10))
answer2.pack(pady=20)
answer3= Label(root, text="", font=("Helvetica", 10))
answer3.pack(pady=20)


#--------------------------------------------------------------------
# Boton1
myButton = Button(root, text="Validar", command=clic)
myButton.pack(pady=20)
root.mainloop()
