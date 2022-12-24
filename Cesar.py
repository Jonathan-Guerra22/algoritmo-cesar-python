from tkinter import *

Main_window = Tk()
Main_window.eval('tk::PlaceWindow . center')

Main_window.geometry('300x300')
Main_window.title("Algoritmo de Cesar")

abcMayusc ="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
abcMinusc = "abcdefghijklmnñopqrstuvwxyz"

abcIndex = len(abcMayusc) - 1
abcLen = len(abcMayusc)


textoFinal = ""

def descifrarFunction():
    texto = textoInicialInput.get()

    corrimiento = int(corrimientoInput.get())

    result = ""

    try:
        for c in texto:
            if c in abcMinusc:
                # quitar la siguiente linea si no importa si ingresan caracteres especiales
                print("letra :: ",abcMinusc.index(c))
                if abcMinusc.index(c) - corrimiento % abcIndex < 0 :
                    result += abcMinusc[(abcMinusc.index(c) + abcLen - corrimiento % abcIndex)]
                else:
                    result += abcMinusc[(abcMinusc.index(c) - corrimiento % abcIndex)]
            elif c in abcMayusc:
                # quitar la siguiente linea si no importa si ingresan caracteres especiales
                print("letra :: ",abcMayusc.index(c))
                if abcMayusc.index(c) - corrimiento % abcIndex < 0 :
                    result += abcMayusc[(abcMayusc.index(c) + abcLen - corrimiento % abcIndex)]
                else:
                    result += abcMayusc[(abcMayusc.index(c) - corrimiento % abcIndex)]
            else:
                result += c
    except:
        return None

    print("texto a descifrar: ",texto)
    print("texto descifrado: ",result)
    return result



def cifrarFunction():
    texto = textoInicialInput.get()

    corrimiento = int(corrimientoInput.get())

    result = ""

    try:
        for c in texto:
            if c in abcMinusc:
                # quitar la siguiente linea si no importa si ingresan caracteres especiales
                print("letra :: ",abcMinusc.index(c))
                if abcMinusc.index(c) + corrimiento > abcIndex:
                    result += abcMinusc[(abcMinusc.index(c) - abcLen + corrimiento % abcIndex)]
                else:
                    result += abcMinusc[(abcMinusc.index(c) + corrimiento % abcIndex)]
            elif c in abcMayusc:
                # quitar la siguiente linea si no importa si ingresan caracteres especiales
                print("letra :: ",abcMayusc.index(c))
                if abcMayusc.index(c) + corrimiento > abcIndex:
                    result += abcMayusc[(abcMayusc.index(c) - abcLen + corrimiento % abcIndex)]
                else:
                    result += abcMayusc[(abcMayusc.index(c) + corrimiento % abcIndex)]
            else:
                result += c
    except:
        return None

    print("texto sin cifrado: ",texto)
    print("texto cifrado: ",result)
    return result


def validaciones(typeCrypt):

    if corrimientoInput.get() == "0":
        resultadoLabel.config(text = "Valor invalido de corrimiento no puede ser 0")
        return None

    if corrimientoInput.get() == "":
        resultadoLabel.config(text = "Valor invalido de corrimiento")
        return None

    if textoInicialInput.get() == "" and typeCrypt == 0:
        resultadoLabel.config(text = "Valor invalido para cifrar")
        return None
    elif textoInicialInput.get() == "" and typeCrypt == 1:
        resultadoLabel.config(text = "Valor invalido para descifrar")
        return None
    elif textoInicialInput.get() == "":
        resultadoLabel.config(text = "Valor invalido para cifrar/descifrar")
        return None
    
    return 0


def cifrar():
    global textoFinal

    if validaciones(0) == None:
        return

    print("Cifrar")
    result = cifrarFunction()
    if result == None:
        resultadoLabel.config(text = "Ocurrrio un problema, no se puedo cifrar")
        return
    resultadoLabel.config(text = result)

def descifrar():
    global textoFinal

    if validaciones(1) == None:
        return

    print("Descifrar")
    result = descifrarFunction()
    if result == None:
        resultadoLabel.config(text = "Ocurrrio un problema, no se puedo descifrar")
        return
    resultadoLabel.config(text = result)



cifrarBoton = Button(Main_window,text = "Cifrar",command = cifrar)
cifrarBoton.place(x=50, y=140)
descifrarBoton = Button(Main_window,text = "Descifrar",command = descifrar)
descifrarBoton.place(x=150, y=140)                



palabraLabel = Label(Main_window,text = "Ingrese la palabra a cifrar/descifrar")
palabraLabel.place(x=10,y=10)

textoInicialInput = Entry(Main_window)
textoInicialInput.place(x=20,y=40)
textoInicialInput.focus_force()


corrimientoLabel = Label(Main_window,text = "Ingrese el valor de corrimiento")
corrimientoLabel.place(x=10,y=70)

corrimientoInput = Entry(Main_window)
corrimientoInput.place(x=20,y=100)



resultadoTitleLabel = Label(Main_window,text = "Resultado : ")
resultadoTitleLabel.place(x=20,y=180)

resultadoLabel = Label(Main_window,text = "", bg='white')
resultadoLabel.place(x=90,y=180)

Main_window.mainloop()
