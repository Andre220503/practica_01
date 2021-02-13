def area_perimetro(longitud, ancho):
    if longitud == ancho:
        area = longitud * ancho
        print(f'El área del cuadrado es: {area}')
    else:
        perimetro = longitud * 2 + ancho * 2
        print(f'El perímetro del rectangulo es: {perimetro}')

lon = float(input("Ingresa la longitud: "))
an = float(input("Ingresa el ancho: "))
area_perimetro(lon,an)