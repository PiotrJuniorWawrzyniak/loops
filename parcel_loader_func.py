def calculate_empty_weight(parcel_weight):
    return 20 - parcel_weight


def send_parcel(parcel_weight, sent_parcels, total_empty_weight, packages):
    empty_weight = calculate_empty_weight(parcel_weight)
    print(f'Wysylam paczke {sent_parcels + 1} o wadze {parcel_weight} kg, puste kg: {empty_weight}')
    total_empty_weight += empty_weight
    parcel_weight = 0
    sent_parcels += 1
    packages.append(empty_weight)
    return parcel_weight, sent_parcels, total_empty_weight, packages


def main():
    elements_amount = int(input('Ile elementow wysylasz: '))
    sent_parcels = 0
    parcel_weight = 0
    total_empty_weight = 0
    packages = []

    for element in range(1, elements_amount + 1):
        element_weight = float(input(f'Podaj wage elementu {element} [1 - 10 kg]: '))

        if element_weight < 1 or element_weight > 10:
            print('Waga elementu musi być z zakresu od 1 do 10 kg.')
            if parcel_weight > 0:
                parcel_weight, sent_parcels, total_empty_weight, packages = send_parcel(
                    parcel_weight, sent_parcels, total_empty_weight, packages)
                parcel_weight = 0
            break

        if parcel_weight + element_weight > 20:
            parcel_weight, sent_parcels, total_empty_weight, packages = send_parcel(
                parcel_weight, sent_parcels, total_empty_weight, packages)
            parcel_weight = element_weight
        else:
            parcel_weight += element_weight

    if parcel_weight > 0:
        parcel_weight, sent_parcels, total_empty_weight, packages = send_parcel(
            parcel_weight, sent_parcels, total_empty_weight, packages)

    if packages:
        max_empty_weight = max(packages)
        parcel_index = packages.index(max_empty_weight) + 1
    else:
        max_empty_weight = 0
        parcel_index = 0

    total_sent_weight = sent_parcels * 20 - total_empty_weight

    print('\nPodsumowanie:')
    print(f'Wyslano paczek: {sent_parcels}.')
    print(f'Wyslano kilogramow: {total_sent_weight}.')
    print(f'Suma pustych kilogramow: {total_empty_weight}.')
    if total_empty_weight > 0:
        print(f'Najwiecej pustych kg miala paczka {parcel_index}: {max_empty_weight}')


if __name__ == "__main__":
    main()
