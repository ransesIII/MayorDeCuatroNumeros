
def main():
    #try:
        N = input(f'ingresa 4 numeros cualesquiera: ')
        delimiter = ' '
        numero = N.split(delimiter)
        
        numero_2 = list(map(int, numero)) # En Python, la función map nos permite aplicar una función sobre los items de un objeto iterable, sintaxis: map(function, objeto iterable)
        numero_2.sort()
        print(f'Escribiste los siguientes numeros {numero}')

        salida = numero_2[3]
        print(f'El {salida} es el mayor')
       
    #except:
    #    print('Ingresa solo numeros')
if __name__=='__main__':
    main()