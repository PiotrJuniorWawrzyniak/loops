elements_amount = int(input('Ile elementow wysylasz: '))

sent_parcels = 0
parcel_weight = 0
total_sent_weight = 0
total_empty_weight = 0
max_empty_weight = 0
parcel_index = 0
empty_weight = 0
packages = []

for element in range(1, elements_amount + 1):
    element_weight = float(
        input(f'Podaj wage elementu {element} [1 - 10 kg]: ')
    )
    if parcel_weight + element_weight > 20:
        print(f'Wysylam paczke {sent_parcels + 1} o wadze {parcel_weight} kg, '
              f'puste kg: {20 - parcel_weight}')
        empty_weight = 20 - parcel_weight
        total_empty_weight += 20 - parcel_weight
        parcel_weight = element_weight
        sent_parcels += 1
        packages.append(empty_weight)
    elif element_weight < 1 or element_weight > 10:
        print('Waga nieprawidlowa.')
        break
    else:
        parcel_weight += element_weight

if parcel_weight > 0:
    print(f'Wysylam paczke {sent_parcels + 1} o wadze {parcel_weight} kg, '
          f'puste {20 - parcel_weight} kg.')
    total_empty_weight += 20 - parcel_weight
    empty_weight = 20 - parcel_weight
    parcel_weight = 0
    sent_parcels += 1

packages.append(empty_weight)

max_empty_weight = max(packages)

parcel_index = packages.index(max(packages)) + 1

total_sent_weight = sent_parcels * 20 - total_empty_weight

print('\nPodsumowanie:')
print(f'Wyslano paczek: {sent_parcels}.')
print(f'Wyslano kilogramow: {total_sent_weight}.')
print(f'Suma pustych kilogramow: {total_empty_weight}.')
if total_empty_weight > 0:
    print(
        f'Najwiecej pustych kg miala paczka {parcel_index}: {max_empty_weight}'
    )
