
def main():
    N = list(input('ingresa 4 numeros cualesquiera: '))
    print(f'Escribiste los siguientes numeros {N}')

    if len(N) == 4:
        if (N[0] > N[1] and (N[0] > N[2]) and (N[0] > N[3])):
            print(f'{N[0]} es el mayor de los 4 numeros')
        elif (N[1] > N[0] and (N[1] > N[2]) and (N[1] > N[3])):
            print(f'{N[1]} es el mayor de los 4 numeros')
        elif (N[2] > N[0] and (N[2] > N[1]) and (N[2] > N[3])):
            print(f'{N[2]} es el mayor de los 4 numeros')
        elif (N[3] > N[0] and (N[3] > N[1]) and (N[3] > N[2])):
            print(f'{N[3]} es el mayor de los 4 numeros')  
    else:
        print('Ingresa solo 4 numeros')
if __name__=='__main__':
    main()