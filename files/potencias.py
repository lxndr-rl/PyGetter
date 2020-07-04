#Archivo de: lxndr.live

ini = 1                    #INICIA CON
end = 50                    #TERMINA EN

end = end+1
ran = range(ini,end,1)

for i in ran:
    pot = 5**i
    print('5 elevado a la',i,'es igual a:', pot)
print('\n\tFin del programa')
