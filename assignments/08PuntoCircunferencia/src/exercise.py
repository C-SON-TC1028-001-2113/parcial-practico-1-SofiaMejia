
import math 
def main():
    # Escribe tu código abajo de esta línea
        r = float(input('Introduce el radio: '))
        x1 = float(input('Introduce x1: '))
        y1 = float(input('Introduce y1: '))
        x2 = float(input('Introduce x2: '))
        y2 = float(input('Introduce y2: '))
        distancia = math.sqrt(((x2-x1)**2)+(y2-y1)**2)
        if distancia ==r:
            print(str('SOBRE'))
        elif distancia <r:
            print(str('DENTRO'))
        else: 
            print(str('FUERA'))

if __name__ == '__main__':
    main()
