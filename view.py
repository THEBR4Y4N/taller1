from tkinter import *
import model as m
import  controller as c

model = m.Ingreso()
controller = c.Validador()

root = Tk()
root.title('PROYECTO DE I-CORTE')
root.geometry("800x800")

# funcion1
def clic():
    Str()
    Int()
    Mail()
    Not()

def Str():
        ingresado = str(e.get())
        model.setEntrada1(ingresado)
        validador = controller.validador_nombres(model)
        if bool(validador) == True:
            answer.config(text="Cadena de caracteres escrita correctamente", fg='#256614')
        else:
            answer.config(text="Cadena de caracteres escrita incorrectamente, por favor intentalo nuevamente..", fg='#C33819')     


def Int():
        ingresado = str(e2.get())
        model.setEntrada2(ingresado)
        validador = controller.validador_numeros(model)
        if bool(validador) == True:
            answer2.config(text="Numero escrito correctamente",fg='#256614')
        else:
            answer2.config(text="Dato Númerico escrito incorrectamente, por favor intentalo nuevamente..",fg='#C33819')


def Mail():
        ingresado = str(e3.get())
        model.setEntrada3(ingresado)
        validador = controller.validador_correos(model)
        if bool(validador) == True:
            answer3.config(text="Correo electronico escrito correctamente",fg='#256614')
        else:
            answer3.config(text="El correo no cumple con el formato correcto (usuario@dominio),por favor intentalo nuevamente..",fg='#C33819')

def Not():
        ingresado = str(e4.get())
        model.setEntrada4(ingresado)
        validador = controller.validador_notacion(model)
        if bool(validador) == True:
            answer4.config(text="Notación cientifica escrita correctamente",fg='#256614')
        else:
            answer4.config(text="Notación cientifica escrita incorrectamente, por favor intentalo nuevamente..",fg='#C33819')

#--------------------------------------------------------------------
# Titulo_Principal
my_label1 = Label(root, text="Validador de expresiones regulares",font=("Helvetica", 20))
my_label1.pack(pady=20)

#--------------------------------------------------------------------
# Titulo_1
my_label2 = Label(root, text="Cadena de Caracteres", font=("Helvetica", 10))
my_label2.pack(pady=20)
# campo1
e = Entry(root, width=40, font=("Arial", 10))
e.pack()
#response1
answer= Label(root, text="", font=("Helvetica", 10))
answer.pack(pady=20)

#--------------------------------------------------------------------
# Titulo_2
my_label3 = Label(root, text="Números",font=("Helvetica", 10))
my_label3.pack(pady=20)
# campo2
e2 = Entry(root, width=40, font=("Arial", 10))
e2.pack()
#response2
answer2= Label(root, text="", font=("Helvetica", 10))
answer2.pack(pady=20)

#--------------------------------------------------------------------
# Titulo_4
my_label5 = Label(root, text="Notación Cientifica", font=("Helvetica", 10))
my_label5.pack(pady=20)
# campo4
e4 = Entry(root, width=40, font=("Arial", 10),)
e4.pack()
#response4
answer4= Label(root, text="", font=("Helvetica", 10))
answer4.pack(pady=20)

#--------------------------------------------------------------------
# Titulo_3
my_label4 = Label(root, text="Correo Electronico", font=("Helvetica", 10))
my_label4.pack(pady=20)
# campo3
e3 = Entry(root, width=40, font=("Arial", 10),)
e3.pack()
#response3
answer3= Label(root, text="", font=("Helvetica", 10))
answer3.pack(pady=20)

#--------------------------------------------------------------------
# Boton
myButton = Button(root, text="Validar", command=clic)
myButton.pack(pady=20)
root.mainloop()
