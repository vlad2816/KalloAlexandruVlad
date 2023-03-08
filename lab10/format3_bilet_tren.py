ticket = {
    's_plecare' : 'Cluj Napoca',
    's_sosire' : 'Costinesti',
    'data_plecare': '27.02.2023',
    'data_sosire': '27.02.2023',
    'ora_plecare': '19:30',
    'ora_sosire': '23:30',
    'pret': 98.45,
    'loc': True,
    'vagon': '3',
    'scaun' : '34'

}
#TEMPLATE_TREN = ('Trenul pleaca din {s_plecare} in data de {data_plecare}'
                 #'la ora {ora_plecare}  si ajunge la {ora_sosire}'
                 #' in data de{data_sosire} la ora {ora_sosire}')

#print(TEMPLATE_TREN.format(**ticket))

print('*' * 70)

print('{:-^70}'.format(ticket['s_plecare']))
print('Data  plecare: {:>55} '.format(ticket['data_plecare']))
print('Ora_plecare: {:>57}'.format(ticket['ora_plecare']))
print('{:-^70}'.format(ticket['s_sosire']))
print('Data  sosire: {:>56} '.format(ticket['data_sosire']))
print('Ora_sosire: {:>58}'.format(ticket['ora_sosire']))

if ticket['loc']:
    print('{:-^70}'.format('Detalii loc'))
    print('*{:^68}*'.format(f'Vagon:{ticket["vagon"]}'))
    print('*{:^68}*'.format(f'Scaun:{ticket["scaun"]}'))

print('Pret: {:.5}  Ron'.format(ticket['pret']))


print('')
print('*' * 70)


