numerolf = 12

if numerolf < 0:
    print('El nunmero es negativo')
elif numerolf > 0:
    print('El numero es positivo')
else:
    print('El numero es 0')


numeroWhile = 0
while numeroWhile < 3:
    numeroWhile +=1
    print(numeroWhile)


# En Python no hay Do/While por ello uso While True

numeroWhile = 0
while True:
    if numeroWhile < 3:
        numeroWhile += 1
    if numeroWhile >= 3:
        break
print(numeroWhile)


numeroFor = 0
for n in range(3):
    numeroFor += 1
    print(numeroFor)


# En Python no hay Switch por ello uso If, Elif, Else

estacion = 'VERANO'

if estacion == 'VERANO':
    print('Es verano')
elif estacion == 'INVIERNO':
    print('Es invierno')
elif estacion == 'OTOÑO':
    print('Es otoño')
else:
    print('Es primavera')