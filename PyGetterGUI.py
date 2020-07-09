#importar librerías START
from tkinter import *
import requests
import json
import os
import urllib.request
from tkinter import scrolledtext
import os.path
from tkinter import ttk
from tkinter import messagebox
from os import startfile
import tkinter as tk
#importar librerías END

#CLASS SCROLL
class Scrollable(tk.Frame):

    def __init__(self, frame, width=16):
        scrollbar = tk.Scrollbar(frame, width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.canvas.yview)
        self.canvas.bind('<Configure>', self.__fill_canvas)
        tk.Frame.__init__(self, frame)
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)
    def __fill_canvas(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)
    def update(self):
        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))
#END CLASS SCROLL

#START def getFile   (Obtiene el archivo de mi servidor)
def getFile():
    re = requests.get('https://api.lxndr.live/pygetter?id='+ v.get())       #Obtiene el JSON de mi API
    dict_json=json.loads(json.dumps(re.json()))                             #Carga el JSON para ser parseado
    error = dict_json['id']                                                 #Extrae el valor de "id"
    url = dict_json['url']                                                  #Extrae el valor de "url"
    autor = dict_json['author']                                             #Extrae el valor de "author"
    file = dict_json['filename']                                            #Extrae el valor de "filename"
    fp = urllib.request.urlopen(url)                                        #Abre el archivo .py alojado en mi servidor
    mybytes = fp.read()                                                     #El archivo . es leído y almacenado
    mystr = mybytes.decode('utf8')                                          #Se lo decodifica en UTF-8 (Para los acentos)
    fp.close()                                                              #Se cierra la conexión con mi servidor

    path = f'C:/Users/{username}/Desktop/PyGetter'                          #Ruta de PyGetter (WINDOWS)
    if os.path.isdir(path):                                                 #Verifica si existe la ruta
        pass                                                                #Esta función literalmente no hace nada
    else:
        os.mkdir(path)                                                      #Si la ruta no existe la crea
    #START def saveDef  (Para guardar los archivos)
    def saveDef():
        autorPath =f'{path}/{autor}/'                                       #Ruta donde se guardan los archivos (WINDOWS)
        if os.path.isdir(autorPath):                                        #Verifica si existe la ruta (para guardar cada archivo en la carpeta de autor)
            pass                                                            #Esta función literalmente no hace nada
        else:
            os.mkdir(autorPath)                                             #Si la ruta no existe la crea
        filePath = f'{autorPath}/{file}'                                    #Ruta completa (PyGetter/autor/file nombre de archivo.py)
        with open(filePath, 'wb') as f:                                     #Crea el archivo si no existe y si existe lo sobreescribe (No debe pasar porque son nombre únicos)
            f.write(mybytes)                                                #Escribe el contenido del archivo
        f.close()                                                           #Cierra el archivo guardado
    #END def saveDef
    #START def runDef  (Correr programa en la consola de fondo)
    def runDef():
        saveDef()
        exec(mybytes)
    #END def runDef
    if error=='error':                                                      #Si la id de la solicitud es 'error' el API lo marca como archivo que no existe
        messagebox.showinfo('404', 'Archivo no encontrado')                 #Muestra el dialogo de alerta
    else:                                                                   #Si encuentra el archivo entonces continúa
        newW = Tk()                                                         #Para la creación de una nueva ventana
        newW.title(autor)                                                   #El título de la ventana es el nombre del autor (Lo provee la API)
        newW.geometry('1000x700')                                           #El tamaño de la nueva ventana
        newW.resizable(width=False, height=False)                           #Bloquea que se cambie el tamaño de la nueva ventana
        #newW.iconphoto(False, photo)                                       #Para el ícono de ventana
        code = scrolledtext.ScrolledText(newW,height=70,width=100)          #Se crea un ScrolledText   (Para mostrar el código)
        code.grid(column=0,row=0)                                           #Se implementa el ScrolledText
        code.insert(INSERT,mybytes)                                         #Se inserta el contenido del archivo de código
        code.configure(state='disabled')                                    #Se desactiva la modificación de texto en el ScrolledText
        runbtn = Button(newW, text='Ejecutar', command=runDef)              #Se crea el botón para ejecutar el programa
        runbtn.grid(column=2,row=0)                                         #Se implementa el botón para ejecutar el programa
        savebtn = Button(newW, text='Guardar Archivo', command=saveDef)     #Se crea el botón para guardar el programa
        savebtn.grid(column=1,row=0)                                        #Se implementa el botón para guardar el programa
#END def getFile
username = os.getlogin()                                                    #Se obtiene el nombre del usuario
liste = requests.get('https://api.lxndr.live/pygetter/listener.php')        #Se obtiene la lista de archivos que existen en mi API
listener=json.loads(json.dumps(liste.json()))                               #Carga el JSON para ser parseado
estruc = ''                                                                 #Se define la variable 'estruc' con la finalidad de más adelante armar la estructura
for item in listener['entries']:                                            #Se hace el recorrido por el JSON del listener.php
    id = (item['id'])                                                       #Se obtiene la id
    autor = (item['autor'])                                                 #Se obtiene el autor
    url = (item['url'])                                                     #Se obtiene la url
    filename = (item['filename'])                                           #Se obtiene el nombre de archivo
    estructura = id+'.- '+filename+'\n\tDe: '+autor+'\n'                    #Se arma la pre-estructura de lo que se va a mostrar
    estruc = '\n'+estructura+estruc                                         #Se arma la estructura final para mostrar la lista de archivos con su id y autor

window = Tk()                                                               #Para la creación de la ventana principal
window.title('PyGetter')                                                    #Título de la ventana "PyGetter"
window.geometry('500x400')                                                  #El tamaño de la ventana principal
window.resizable(width=False, height=False)                                 #Bloquea que se cambie el tamaño de la ventana
header = ttk.Frame(window)                                                  #Crea un cuadro en la parte superior
header.pack()                                                               #Se implementa el cuadro
#photo = PhotoImage(file = 'icon.png')                                      #Icono a usar para la ventana
#window.iconphoto(False, photo)                                             #Implementa icono
scrollable_body = Scrollable(window, width=10)                              #Se crea el cuerpo Scrollable

selection=Label(scrollable_body, text =estruc,font = 'Arial').grid()        #Se escribe dentro del scrollable_body la lista de archivos
scrollable_body.update()                                                    #scrollable_body se actualiza para mostrar los archivos

v = StringVar()                                                             #Se define un StringVar para poder modificar la entrada más veces
e = Entry(header, textvariable=v).pack()                                    #Se crea e implementa la caja de entrar (para ingresar texto)

ttk.Button(header, text ='Obtener Archivo', command=getFile).pack()         #Se crea e implementa el botón en el cuadro superior de la ventana principal

window.mainloop()                                                           #Mainloop ^-^
