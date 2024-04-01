number = int(input('Podaj liczbe od 1 do 100: '))

if number < 1 or number > 100:
    print('Liczba musi byc z przedzialu od 1 do 100.')
else:
    print(f'Ciag Collatza dla liczby {number}: {number}', end=' ')
    length = 1

    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1

        print(f'{number}', end=' ')

        length += 1

    print(f'\nDlugosc ciagu Collatza wynosi {length}.')

    print(f'\nDlugosc ciagu Collatza dla liczby {number} wynosi {length}.')

    # Nie umiem sprawic, zeby w/w komenda printowala liczbe podana na wejsciu
    # przez uzytkownika, zawsze printuje dlugosc ciagu dla liczby '1'.
