'''
Autor: Daniel Espinoza (@paleta_chupada)
Version: 1.0
Descripcion: Cifrador de Cesar para alfabeto en ingles (mod 26)
'''

import ntpath
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import functools
from Crypto.Cipher import DES
import base64

# Funcion para abrir el explorador y guardar la ruta
def browseFiles(): 
    ruta = filedialog.askopenfilename(initialdir = "D:/Documentos/ESCOM/7moSemestre/Crypto/Practica 1/", title = "Select a File", filetypes = (("Text files", "*.bmp*"), ("all files", "*.*")))
    labelInfo = Label(principal, text="Ruta del archivo: ")
    labelInfo.place(x=150,y=0) 
    labelExplorador.configure(text=ruta)

# Funcion de decifrado
def secundaria_v(master,  callback=None, args=(), kwargs={}):

    # Funcion para cifrar en ECB
    def cifrarECB():
        ruta = labelExplorador.cget("text") # Obtenemos la direccion del archivo
        nombre = str(ntpath.basename(ruta)) # Obtenemos su nombre
        ruta_aux = str(ruta).replace(nombre,"") # Eliminamos el nombre de la ruta
        nombre = nombre.replace(".bmp","") # Eliminamos su extension del nombre

        # Obtenemos la clave y la convertimos a bytes
        clave=numero.get()
        clave=clave.encode('utf-8')

        # Inicializamos el cifrador
        cifrador = DES.new(clave,DES.MODE_ECB)

        # Abrimos la image e inicializamos la imagen cifrada
        img_or = open(ruta,"rb")
        img_en = open(ruta_aux+nombre+"_eECB.bmp","wb")
        
        # Escribimos el principio de la imagen
        data = img_or.read(54)
        img_en.write(data)

        # Obtenemos el tamanio de la imagen
        img_or.seek(34)
        size = int.from_bytes(img_or.read(4),byteorder='little')

        # Nos posicionamos en el inicio de la imagen
        img_or.seek(54)

        # Ciframos cada 8 bytes
        i=0
        while i<size:
            pixels = img_or.read(8)
            encrypted_pixels = cifrador.encrypt(pixels)
            img_en.write(encrypted_pixels)
            i=i+8
        
        print("Imagen cifrada en ECB")
    
    # Funcion para cifrar en CBC
    def cifrarCBC():
        ruta = labelExplorador.cget("text") # Obtenemos la direccion del archivo
        nombre = str(ntpath.basename(ruta)) # Obtenemos su nombre
        ruta_aux = str(ruta).replace(nombre,"") # Eliminamos el nombre de la ruta
        nombre = nombre.replace(".bmp","") # Eliminamos su extension del nombre

        # Obtenemos la clave y la convertimos a bytes
        clave=numero.get()
        clave=clave.encode('utf-8')
        IV=clave

        # Inicializamos el cifrador
        cifrador = DES.new(clave,DES.MODE_CBC,IV)

        # Abrimos la image e inicializamos la imagen cifrada
        img_or = open(ruta,"rb")
        img_en = open(ruta_aux+nombre+"_eCBC.bmp","wb")
        
        # Escribimos el principio de la imagen
        data = img_or.read(54)
        img_en.write(data)

        # Obtenemos el tamanio de la imagen
        img_or.seek(34)
        size = int.from_bytes(img_or.read(4),byteorder='little')

        # Nos posicionamos en el inicio de la imagen
        img_or.seek(54)

        # Ciframos cada 8 bytes
        i=0
        while i<size:
            pixels = img_or.read(8)
            encrypted_pixels = cifrador.encrypt(pixels)
            img_en.write(encrypted_pixels)
            i=i+8
        
        print("Imagen cifrada en CBC")
    
    # Funcion para cifrar en CFB
    def cifrarCFB():
        ruta = labelExplorador.cget("text") # Obtenemos la direccion del archivo
        nombre = str(ntpath.basename(ruta)) # Obtenemos su nombre
        ruta_aux = str(ruta).replace(nombre,"") # Eliminamos el nombre de la ruta
        nombre = nombre.replace(".bmp","") # Eliminamos su extension del nombre

        # Obtenemos la clave y la convertimos a bytes
        clave=numero.get()
        clave=clave.encode('utf-8')
        IV=clave

        # Inicializamos el cifrador
        cifrador = DES.new(clave,DES.MODE_CFB,IV)

        # Abrimos la image e inicializamos la imagen cifrada
        img_or = open(ruta,"rb")
        img_en = open(ruta_aux+nombre+"_eCFB.bmp","wb")
        
        # Escribimos el principio de la imagen
        data = img_or.read(54)
        img_en.write(data)

        # Obtenemos el tamanio de la imagen
        img_or.seek(34)
        size = int.from_bytes(img_or.read(4),byteorder='little')

        # Nos posicionamos en el inicio de la imagen
        img_or.seek(54)

        # Ciframos cada 8 bytes
        i=0
        while i<size:
            pixels = img_or.read(8)
            encrypted_pixels = cifrador.encrypt(pixels)
            img_en.write(encrypted_pixels)
            i=i+8
        
        print("Imagen cifrada en CFB")
    
    # Funcion para cifrar en OFB
    def cifrarOFB():
        ruta = labelExplorador.cget("text") # Obtenemos la direccion del archivo
        nombre = str(ntpath.basename(ruta)) # Obtenemos su nombre
        ruta_aux = str(ruta).replace(nombre,"") # Eliminamos el nombre de la ruta
        nombre = nombre.replace(".bmp","") # Eliminamos su extension del nombre

        # Obtenemos la clave y la convertimos a bytes
        clave=numero.get()
        clave=clave.encode('utf-8')
        IV=clave

        # Inicializamos el cifrador
        cifrador = DES.new(clave,DES.MODE_OFB,IV)

        # Abrimos la image e inicializamos la imagen cifrada
        img_or = open(ruta,"rb")
        img_en = open(ruta_aux+nombre+"_eOFB.bmp","wb")
        
        # Escribimos el principio de la imagen
        data = img_or.read(54)
        img_en.write(data)

        # Obtenemos el tamanio de la imagen
        img_or.seek(34)
        size = int.from_bytes(img_or.read(4),byteorder='little')

        # Nos posicionamos en el inicio de la imagen
        img_or.seek(54)

        # Ciframos cada 8 bytes
        i=0
        while i<size:
            pixels = img_or.read(8)
            encrypted_pixels = cifrador.encrypt(pixels)
            img_en.write(encrypted_pixels)
            i=i+8
        
        print("Imagen cifrada en OFB")

    # Creamos interfaz para que el usario ingrese la clave
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    labelEspacio3 = Label(main_frame, text="")
    labelClave = Label(main_frame, text="Ingresa la llave (8 bytes en hexadecimal)", height=4)
    numero = Entry(main_frame)
    buttonCifrarECB = Button(main_frame, text="Cifrar en ECB", command = cifrarECB)
    buttonCifrarCBC = Button(main_frame, text="Cifrar en CBC", command = cifrarCBC)
    buttonCifrarCFB = Button(main_frame, text="Cifrar en CFB", command = cifrarCFB)
    buttonCifrarOFB = Button(main_frame, text="Cifrar en OFB", command = cifrarOFB)
    buttonRegresar = Button(main_frame, text = "Regresar", command = callback)
    labelClave.pack()
    numero.pack()
    labelEspacio3.pack()
    buttonCifrarECB.pack()
    buttonCifrarCBC.pack()
    buttonCifrarCFB.pack()
    buttonCifrarOFB.pack()
    buttonRegresar.pack()

    return main_frame

def tercera_v(master,  callback=None, args=(), kwargs={}):
    
    # Funcion para descifrar ECB
    def decifrarECB():
        ruta = labelExplorador.cget("text") # Obtenemos la direccion del archivo
        nombre = str(ntpath.basename(ruta)) # Obtenemos su nombre
        ruta_aux = str(ruta).replace(nombre,"") # Eliminamos el nombre de la ruta
        nombre = nombre.replace("_DES.bmp","") # Eliminamos su extension del nombre

        # Obtenemos la clave y la convertimos a bytes
        clave=numero.get()
        clave=clave.encode('utf-8')

        # Inicializamos el cifrador
        cifrador = DES.new(clave,DES.MODE_ECB)

        # Abrimos la image e inicializamos la imagen cifrada
        img_or = open(ruta,"rb")
        img_en = open(ruta_aux+nombre+"_dECB.bmp","wb")
        
        # Escribimos el principio de la imagen
        data = img_or.read(54)
        img_en.write(data)

        # Obtenemos el tamanio de la imagen
        img_or.seek(34)
        size = int.from_bytes(img_or.read(4),byteorder='little')

        # Nos posicionamos en el inicio de la imagen
        img_or.seek(54)

        # Desciframos cada 8 bytes
        i=0
        while i<size:
            pixels = img_or.read(8)
            encrypted_pixels = cifrador.decrypt(pixels)
            img_en.write(encrypted_pixels)
            i=i+8
        
        print("Imagen descifrada en ECB")

    # Funcion para descifrar CBC
    def decifrarCBC():
        ruta = labelExplorador.cget("text") # Obtenemos la direccion del archivo
        nombre = str(ntpath.basename(ruta)) # Obtenemos su nombre
        ruta_aux = str(ruta).replace(nombre,"") # Eliminamos el nombre de la ruta
        nombre = nombre.replace("_DES.bmp","") # Eliminamos su extension del nombre

        # Obtenemos la clave y la convertimos a bytes
        clave=numero.get()
        clave=clave.encode('utf-8')
        IV=clave

        # Inicializamos el cifrador
        cifrador = DES.new(clave,DES.MODE_CBC,IV)

        # Abrimos la image e inicializamos la imagen cifrada
        img_or = open(ruta,"rb")
        img_en = open(ruta_aux+nombre+"_dCBC.bmp","wb")
        
        # Escribimos el principio de la imagen
        data = img_or.read(54)
        img_en.write(data)

        # Obtenemos el tamanio de la imagen
        img_or.seek(34)
        size = int.from_bytes(img_or.read(4),byteorder='little')

        # Nos posicionamos en el inicio de la imagen
        img_or.seek(54)

        # Desciframos cada 8 bytes
        i=0
        while i<size:
            pixels = img_or.read(8)
            encrypted_pixels = cifrador.decrypt(pixels)
            img_en.write(encrypted_pixels)
            i=i+8
        
        print("Imagen descifrada en CBC")

    # Funcion para descifrar CFB
    def decifrarCFB():
        ruta = labelExplorador.cget("text") # Obtenemos la direccion del archivo
        nombre = str(ntpath.basename(ruta)) # Obtenemos su nombre
        ruta_aux = str(ruta).replace(nombre,"") # Eliminamos el nombre de la ruta
        nombre = nombre.replace("_DES.bmp","") # Eliminamos su extension del nombre

        # Obtenemos la clave y la convertimos a bytes
        clave=numero.get()
        clave=clave.encode('utf-8')
        IV=clave

        # Inicializamos el cifrador
        cifrador = DES.new(clave,DES.MODE_CFB,IV)

        # Abrimos la image e inicializamos la imagen cifrada
        img_or = open(ruta,"rb")
        img_en = open(ruta_aux+nombre+"_dCFB.bmp","wb")
        
        # Escribimos el principio de la imagen
        data = img_or.read(54)
        img_en.write(data)

        # Obtenemos el tamanio de la imagen
        img_or.seek(34)
        size = int.from_bytes(img_or.read(4),byteorder='little')

        # Nos posicionamos en el inicio de la imagen
        img_or.seek(54)

        # Desciframos cada 8 bytes
        i=0
        while i<size:
            pixels = img_or.read(8)
            encrypted_pixels = cifrador.decrypt(pixels)
            img_en.write(encrypted_pixels)
            i=i+8
        
        print("Imagen descifrada en CFB")

    # Funcion para descifrar OFB
    def decifrarOFB():
        ruta = labelExplorador.cget("text") # Obtenemos la direccion del archivo
        nombre = str(ntpath.basename(ruta)) # Obtenemos su nombre
        ruta_aux = str(ruta).replace(nombre,"") # Eliminamos el nombre de la ruta
        nombre = nombre.replace("_DES.bmp","") # Eliminamos su extension del nombre

        # Obtenemos la clave y la convertimos a bytes
        clave=numero.get()
        clave=clave.encode('utf-8')
        IV=clave

        # Inicializamos el cifrador
        cifrador = DES.new(clave,DES.MODE_OFB,IV)

        # Abrimos la image e inicializamos la imagen cifrada
        img_or = open(ruta,"rb")
        img_en = open(ruta_aux+nombre+"_dOFB.bmp","wb")
        
        # Escribimos el principio de la imagen
        data = img_or.read(54)
        img_en.write(data)

        # Obtenemos el tamanio de la imagen
        img_or.seek(34)
        size = int.from_bytes(img_or.read(4),byteorder='little')

        # Nos posicionamos en el inicio de la imagen
        img_or.seek(54)

        # Desciframos cada 8 bytes
        i=0
        while i<size:
            pixels = img_or.read(8)
            encrypted_pixels = cifrador.decrypt(pixels)
            img_en.write(encrypted_pixels)
            i=i+8
        
        print("Imagen descifrada en OFB")
    
    # Creamos la tercera interfaz
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    labelEspacio3 = Label(main_frame, text="")
    labelLlave = Label(main_frame, text="Ingresa la llave para decifrar (funcion de cifrado)", height=4)
    numero = Entry(main_frame)
    buttonCifrarECB = Button(main_frame, text="Decifrar ECB", command=decifrarECB)
    buttonCifrarCBC = Button(main_frame, text="Decifrar CBC", command=decifrarCBC)
    buttonCifrarCFB = Button(main_frame, text="Decifrar CFB", command=decifrarCFB)
    buttonCifrarOFB = Button(main_frame, text="Decifrar OFB", command=decifrarOFB)
    buttonRegresar = Button(main_frame, text = "Regresar", command = callback)
    labelLlave.pack()
    numero.pack()
    labelEspacio3.pack()
    buttonCifrarECB.pack()
    buttonCifrarCBC.pack()
    buttonCifrarCFB.pack()
    buttonCifrarOFB.pack()
    buttonRegresar.pack()

    return main_frame
    
# Funcion para mostrar la ventana principal
def mostrar_prin():
    secundaria.pack_forget()
    tercera.pack_forget()
    principal.pack(side="top", fill="both", expand=True)

# Funcion para mostrar la ventana de cifrado
def mostrar_sec():
    principal.pack_forget()
    secundaria.pack(side="top", fill="both", expand=True)

# Funcion para mostrar la ventana de descifrado
def mostrar_ter():
    principal.pack_forget()
    tercera.pack(side="top", fill="both", expand=True)

# Creacion de la ventana y anexo de los botones y los labels                                                                                                       
root = tk.Tk() 
root.title('Practica 0 (Cifrador de Cesar)') 
root.geometry("600x500")
root.resizable(0,0)
principal = tk.Frame(root)
labelEspacio = Label(principal, text="")
labelEspacio2 = Label(principal, text="")
labelExplorador = Label(principal, text = "Selecciona una imagen BMP", height=4)    
buttonBuscar = Button(principal, text = "Buscar", command = browseFiles)
buttonCifrar = Button(principal, text = "Cifrar", command=mostrar_sec)
buttonDescifrar = Button(principal, text = "Descifrar", command=mostrar_ter)  
buttonSalir = Button(principal, text = "Salir", command = exit)  
labelExplorador.pack()
buttonBuscar.pack()
labelEspacio.pack()
buttonCifrar.pack()
buttonDescifrar.pack()
labelEspacio2.pack()
buttonSalir.pack()
secundaria = secundaria_v(root, mostrar_prin)
tercera = tercera_v(root, mostrar_prin)
mostrar_prin()
root.mainloop() 