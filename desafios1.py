number_months = int(input('Você possui quantos meses completos de trabalho? '))
disponibilidade_dos_meses = input('Possui disponibilidade de para tirar férias nos meses de Dezembro ou Janeiro? (Responda com sim ou não) ')

if number_months >= 12 and disponibilidade_dos_meses == 'sim':
    print('Você pode tirar suas férias!')
else:
    print('Você ainda não pode tirar férias.')
