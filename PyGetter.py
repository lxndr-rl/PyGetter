import requests
import json
import os
import urllib.request

liste = requests.get('https://api.lxndr.live/pygetter/listener.php')
listener=json.loads(json.dumps(liste.json()))

print('\n')
for item in listener['entries']:
    id = (item['id'])
    autor = (item['autor'])
    url = (item['url'])
    filename = (item['filename'])
    print(id+'.- '+filename+'\n\tDe: '+autor+'\n')

sel = int(input('Ingrese el id del archivo: '))
sel = str(sel)
re = requests.get('https://api.lxndr.live/pygetter?id='+sel)
dict_json=json.loads(json.dumps(re.json()))
error = dict_json["id"]
url = dict_json["url"]
autor = dict_json["author"]

fp = urllib.request.urlopen(url)
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()

if error=='error':
    print('\nEl archivo no existe')
    os.system("PAUSE")
    exit()

lectura = input('Desea leer el archivo? (S/N): ')
lectura = lectura.lower()
while (lectura !='s' and lectura !='n'):
    print('Ingrese una opción válida')
    lectura = input('Desea leer el archivo? (S/N): ')
    lectura = lectura.lower()
if(lectura=='s'):
    print('\n------INICIA CÓDIGO------\n')
    print(mystr)
    print('\n------TERMINA CÓDIGO------')
    print('\n\n\tAutor: ',autor)
    os.system("PAUSE")
    exit()
else:
    save = input('Desea guardar el archivo? (S/N): ')
    save = save.lower()
    while (save !='s' and save !='n'):
        print('Ingrese una opción válida')
        save = input('Desea guardar el archivo? (S/N): ')
        save = save.lower()
    if(save=='s'):
        with open('files/'+filename, "wb") as f:
            f.write(mybytes)
        f.close()
        print('Archivo Guardado :)')
        os.system("PAUSE")

    else:
        exe = input('Desea ejecutar el archivo? (S/N): ')
        exe = exe.lower()
        while (exe !='s' and exe !='n'):
            print('Ingrese una opción válida')
            exe = input('Desea ejecutar el archivo? (S/N): ')
            exe = exe.lower()
        if(exe=='s'):
            print('\n------INICIA EJECUCIÓN------\n')
            exec(mystr)
            print('\n------TERMINA EJECUCIÓN------')
            os.system("PAUSE")
        else:
            print('\nFin del programa')
            exit()
