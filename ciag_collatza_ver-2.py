number = int(input('Podaj liczbe od 1 do 100: '))
input_number = number

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

    print(
        f'\nDlugosc ciagu Collatza dla liczby {input_number} wynosi {length}.'
    )

# Poprawione wyswietlanie dlugosci ciagu dla liczby podanej przez uzytkownika.
