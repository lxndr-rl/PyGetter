from tkinter import *
import requests
import json
import os
import urllib.request
from tkinter import scrolledtext
import os.path
from tkinter import messagebox
from os import startfile

username = os.getlogin()    # Fetch username

liste = requests.get('https://api.lxndr.live/pygetter/listener.php')
listener=json.loads(json.dumps(liste.json()))
estruc = ''
print('\n')
for item in listener['entries']:
    id = (item['id'])
    autor = (item['autor'])
    url = (item['url'])
    filename = (item['filename'])
    estructura = id+'.- '+filename+'\n\tDe: '+autor+'\n'
    estruc = '\n'+estructura+estruc

window = Tk()
window.title("PyGetter")
window.geometry('500x400')
#photo = PhotoImage(file = "icon.png")
#window.iconphoto(False, photo)

selection = Label(window, text=estruc)
selection.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)


def clicked():
    re = requests.get('https://api.lxndr.live/pygetter?id='+ txt.get())
    dict_json=json.loads(json.dumps(re.json()))
    error = dict_json["id"]
    url = dict_json["url"]
    autor = dict_json["author"]
    #file = open(path,'w')
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    file = dict_json["filename"]

    path = f'C:/Users/{username}/Desktop/PyGetter/{file}'
    isPath = os.path.isfile(path)
    try:
        os.mkdir(f'C:/Users/{username}/Desktop/PyGetter')
    except:
        def saveDef():
            with open(path, "wb") as f:
                f.write(mybytes)
            f.close()
        def runDef():
            saveDef()
            os.system(f"py {path}")
        if error=='error':
            messagebox.showinfo('404', 'Archivo no encontrado')
        else:
            newW = Tk()
            newW.title(autor)
            newW.geometry('1000x700')
            #newW.iconphoto(False, photo)
            code = scrolledtext.ScrolledText(newW,height=70,width=100)
            code.grid(column=0,row=0)
            code.insert(INSERT,mybytes)
            runbtn = Button(newW, text="Ejecutar", command=runDef)
            runbtn.grid(column=2,row=0)
            savebtn = Button(newW, text="Guardar Archivo", command=saveDef)
            savebtn.grid(column=1,row=0)



btn = Button(window, text="Obtener Archivo!", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()
