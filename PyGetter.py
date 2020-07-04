import requests
import json
import os


filename = input('Ingrese el nombre del archivo: ')
format = filename.find(".py")
if(format ==-1):
    filename=filename+'.py'
re = requests.get('https://api.lxndr.live/python?file='+filename)
dict_json=json.loads(json.dumps(re.json()))
error = dict_json["id"]
code = dict_json["code"]
autor = dict_json["author"]
if error=='error':
    print('\nEl archivo no existe')
    exit()

lectura = input('Desea leer el archivo? (S/N): ')
lectura = lectura.lower()
while (lectura !='s' and lectura !='n'):
    print('Ingrese una opción válida')
    lectura = input('Desea leer el archivo? (S/N): ')
    lectura = lectura.lower()
if(lectura=='s'):
    print('\n------INICIA CÓDIGO------\n')
    print(code)
    print('\n------TERMINA CÓDIGO------')
    print('\n\n\tAutor: ',autor)
    exit()
else:
    save = input('Desea guardar el archivo? (S/N): ')
    save = save.lower()
    if(save=='s'):
        f = open ('files/'+filename,'w')
        f. write('#Archivo de: '+autor + os.linesep+ os.linesep)
        f.write(code)
        f.close()
        print('Archivo Guardado :)')

    else:
        exe = input('Desea ejecutar el archivo? (S/N): ')
        exe = exe.lower()
        if(exe=='s'):
            print('\n------INICIA EJECUCIÓN------\n')
            exec(code)
            print('\n------TERMINA EJECUCIÓN------')

        else:
            print('\nFin del programa')
            exit()
