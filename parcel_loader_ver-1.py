elements = int(input('Podaj liczbę elementów do wysłania: '))

parcels = 0
total_weight = 0
total_empty_weight = 0
max_empty_weight = 0
max_empty_parcel_index = -1

for element in range(1, elements + 1):
    element_weight = float(input(
        f'Podaj wage elementu {element} (od 1 do 10 kg): '
    ))

    if element_weight < 1 or element_weight > 10:
        print('Waga elementu musi byc z przedzialu od 1 do 10 kg.')
        continue

    elif total_weight + element_weight > 20:
        print(
            f'Wysylam paczke {parcels + 1} o wadze {total_weight} kg, '
            f'puste {20 - total_weight} kg.'
        )
        total_empty_weight += 20 - total_weight
        total_weight = element_weight
        parcels += 1
    else:
        total_weight += element_weight

empty_weight = max(0, 20 - total_weight)
if empty_weight > max_empty_weight:
    max_empty_weight = empty_weight
    max_empty_parcel_index = parcels + 1

if total_weight > 0:
    print(
        f'Wysylam paczke {parcels + 1} o wadze {total_weight} kg, '
        f'puste {20 - total_weight} kg.'
    )
    total_empty_weight += 20 - total_weight

print('\nPodsumowanie:')
print(f'Wyslano paczek: {parcels + 1}')
print(f'Wyslano kilogramow: {total_weight}')
print(f'Suma pustych kilogramow: {total_empty_weight}')

if max_empty_parcel_index != -1:
    print(f'Najwiecej pustych kilogramow ma paczka '
          f'{max_empty_parcel_index}: {max_empty_weight} kg.')

# 1. Nie umiem dodac w podsumowaniu "Wyslano paczek" wagi poszczegolnych
#   elementow, przypisanych do poszczegolnych paczek.
# 2. W podsumowaniu "Wyslano kilogramow" wyswietla tylko wage ostatniej paczki.
# 3. Jesli wiecej niz jedna paczka ma taka sama maksymalna ilosc pustych kg,
#   w podsumowaniu wyswietla tylko ostatnia z nich.
# 4. W petli for jest continue zamiast break, zeby program sie nie konczyl, a
#   tylko pomijal paczki o niedopuszczlanej wadze.
