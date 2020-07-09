# PyGetter
Hecho por lxndr ubicación de API: https://api.lxndr.live/pygetter?id=

# Instalar dependencias
Dependencia requests
~~~bash
pip install requests
~~~

# Disponibilidad
Por el momento solo funciona con Windows
### Explicación ###
PyGetter está configurado para guardar los archivos en escritorio, por ende se crea carpetas usando 
~~~python
os.mkdir(path)
~~~
donde *path* está definido por
~~~python
path = f'C:/Users/{username}/Desktop/PyGetter'        #username es el nombre del usuario que corre el programa
~~~
esta estructura de archivos está disponible solo en Windows, en la siguiente actualización se detectará el SO y así usar los *path* respectivos
# Contribuciones
Toda contribución **explicada** y que se considere **útil** en la sección de *Pull requests* se aprobará y se darán los créditos respectivos :)








 > *Este código fue hecho como pasatiempo (PHP, MySQL y Python3)*
 
