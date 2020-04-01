# Вариант 18 (3)
# number 915783624
# external: 2руб/минута исходящие звонки, но 20 минут бесплатно
# internal: 0руб/минута входящие,
# SMS: 2руб/шт

import csv
# Initial data
number = 915783624
smscost = 2 # множитель тарифного плана
free_sms = 0 # бесплатных смс

external = 2 # множитель тарифного плана
free_ext = 20 # бесплатных исходящих

internal = 0 # множитель тарифного плана
free_int = 0 # бесплатных входящих

ext = 0
inte = 0
sms = 0
# Парсинг csv и подсчет общей длительности звонков и количества СМС
with open('data.csv') as File:
    reader = csv.reader(File, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[1] == str(number):
            sms += int(row[4])
            ext += float(row[3])
        if row[2] == str(number):
            inte += float(row[3])

# Универсальный подсчет для любых множителей тарифного плана
if sms <= free_sms:
    tarif_sms = 0
else:
    tarif_sms = (sms - free_sms) * smscost

if ext <= free_ext:
    tarif_ext = 0
else:
    tarif_ext = (ext - free_ext) * external

if ext <= free_int:
    tarif_int = 0
else:
    tarif_int = (inte - free_int) * internal

# Счет
with open('bill.txt','w') as out:
    out.write('Bill for number ')
    out.write(str(number))
    out.write('\n')
    out.write('Sms cost: ')
    out.write(str(tarif_sms))
    out.write('roubles\n')
    out.write('External calls cost: ')
    out.write(str(round(tarif_ext, 2)))
    out.write('roubles\n')
    out.write('Internal calls cost: ')
    out.write(str(round(tarif_int, 2)))
    out.write('roubles\n')
    out.write('Total bill is: ')
    out.write(str(round(tarif_ext + tarif_int + tarif_sms, 2)))
    out.write('roubles\n')
