weight = int(input('Weight: '))
unit = input('(K)g or (L)bs: ')

if unit.upper() == 'K':
    converted_weight = weight * 2.20462
    print(f'Your weight is {converted_weight} kg')
else:
    converted_weight = weight * 0.453592
    print(f'Your weight is {converted_weight} lbs')
