from tkinter import *

root = Tk()
root.title('PROYECTO DE I-CORTE')
root.geometry("800x600")

# funcion1


def myclic():
    if my_label == "":
        myLabel = Label(root, text="El texto ingresado no es correcto...")
        myLabel.pack()


# Titulo_1
my_label = Label(root, text="Validador de expresiones regulares",
                 font=("Helvetica", 20))

my_label.pack(pady=20)

# campo1
e = Entry(root, width=50, font=("Arial", 15))
e.pack()

# Boton1
myButton = Button(root, text="validar", command=myclic)
myButton.pack()

root.mainloop()
