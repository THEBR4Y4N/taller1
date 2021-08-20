from tkinter import *

root = Tk()
root.title('PROYECTO DE I-CORTE')
root.geometry("800x600")

# funcion1
def clic():
    Int()
    Float()


def Int():
    try:
            int(e.get())
            answer.config(text="tu edad es un valor entero valido")
    except ValueError:
            answer.config(text="tu edad no es un valor entero valido, intentalo nuevamente")

def Float():
    try:
            float(e2.get())
            answer2.config(text="tu estatura es un valor entero valido")
    except ValueError:
            answer2.config(text="tu estatura no es un valor entero valido, intentalo nuevamente")



# Titulo_Principal
my_label1 = Label(root, text="Validador de expresiones regulares",
                 font=("Helvetica", 20))
my_label1.pack(pady=20)

# Titulo_1
my_label2 = Label(root, text="Ingresa tu edad",
                 font=("Helvetica", 10))
my_label2.pack(pady=20)

# campo1
e = Entry(root, width=40, font=("Arial", 10))
e.pack()

# Titulo_2
my_label3 = Label(root, text="Ingresa tu estatura",
                 font=("Helvetica", 10))
my_label3.pack(pady=20)

# campo2
e2 = Entry(root, width=40, font=("Arial", 10),)
e2.pack()

#response
answer= Label(root, text="", font=("Helvetica", 10))
answer.pack(pady=20)
answer2= Label(root, text="", font=("Helvetica", 10))
answer2.pack(pady=20)

#--------------------------------------------------------------------
# Boton1
myButton = Button(root, text="validar", command=clic)
myButton.pack(pady=20)
root.mainloop()
