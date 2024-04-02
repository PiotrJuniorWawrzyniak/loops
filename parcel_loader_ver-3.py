elements = int(input('Podaj liczbę elementów do wysłania: '))

parcels = 0
total_weight = 0
total_empty_weight = 0
max_empty_weight = 0
max_empty_parcel_index = -1
sum_elements_weight = []

for element in range(1, elements + 1):
    element_weight = float(input(
        f'Podaj wage elementu {element} (od 1 do 10 kg): '
    ))

    if element_weight < 1 or element_weight > 10:
        print('Waga elementu musi byc z przedzialu od 1 do 10 kg.')
        continue

    elif total_weight + element_weight > 20:
        print(
            f'Wysylam paczke {parcels + 1} o wadze {round(total_weight, 2)} '
            f'kg, puste {round(20 - total_weight, 2)} kg.'
        )
        total_empty_weight += 20 - total_weight
        total_weight = element_weight
        parcels += 1
    else:
        total_weight += element_weight

    sum_elements_weight.append(element_weight)

empty_weight = max(0, 20 - total_weight)
if empty_weight > max_empty_weight:
    max_empty_weight = empty_weight
    max_empty_parcel_index = parcels + 1

if total_weight > 0:
    print(
        f'Wysylam paczke {parcels + 1} o wadze {round(total_weight, 2)} kg, '
        f'puste {round(20 - total_weight, 2)} kg.'
    )
    total_empty_weight += 20 - total_weight

print('\nPodsumowanie:')
print(f'Wyslano paczek: {parcels + 1} {tuple(sum_elements_weight)}')
print(f'Wyslano kilogramow: {sum(sum_elements_weight)}')
print(f'Suma pustych kilogramow: {round(total_empty_weight, 2)}')

if max_empty_parcel_index != -1:
    print(f'Najwiecej pustych kilogramow ma paczka {max_empty_parcel_index}: '
          f'{round(max_empty_weight, 2)} kg')

# 1. Dodalem zaokraglenie we wszystkich mozliwych miejscach, ponieważ przy
#    testowaniu wyswietlal wartosci z wieloma miejscami po przecinku, jesli
#    dostawal zmiennoprzecinkowa na wejsciu.

# 2. Poprawilem wyswietlanie sumy wszystkich kilogramow w podsumowaniu.

# 3. Wciaz uzywam 'continue' zamiast 'break', poniewaz po dodaniu pierwszego
#    elementu o niedozwolonej wadze, program wysyla pusta paczke.

# 4. Dodalem w podsumowaniu "Wyslano paczek" wagi poszczegolnych
#    elementow, ale nie umiem przypisac ich do poszczegolnych paczek.

# 5. Zle dziala w podsumowaniu indeks paczek o najwiekszej pustej liczbie kg.
#    Jesli wiecej niz jedna paczka ma taka sama maksymalna ilosc pustych kg,
#    w podsumowaniu wyswietla tylko ostatnia z nich. Co wiecej, w pewnych
#    przypadkach w ogole nie printuje tej informacji, a dokladnie w sytuacji,
#    gdy po drodze sa puste kg, ale ostatnia paczka ich nie ma.
