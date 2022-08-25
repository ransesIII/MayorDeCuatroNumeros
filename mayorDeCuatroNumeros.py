
def main():
    #try:
        N = input(f'ingresa 4 numeros cualesquiera: ')
        delimiter = ','
        numero = N.split(delimiter)
        numero.sort()
        #print(f'Escribiste los siguientes numeros {numero}')

        salida = numero[3]
        print(f'El {salida} es el mayor')

        #for i in numero:
        #    #print(i)
        #    if i >= N[0] and >= N[1] >= N[2] >= N[3]:
        #        print(f'{i} es mayor')
       
    #except:
    #    print('Ingresa solo numeros')
if __name__=='__main__':
    main()