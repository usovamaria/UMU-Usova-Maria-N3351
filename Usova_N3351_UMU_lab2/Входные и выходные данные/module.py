# Лабораторная 2
# Вариант 18 (3)
# k = 1 руб/Мб
# IP 192.168.250.27

import csv
from pylab import *
traffic = 0
tarif = 1 # множитель тарифного плана
datalist = [[]]
time = ''
by = 0

with open('data.csv', 'r') as File:
    reader = csv.reader(File, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[3] == '192.168.250.27' or row[4] == '192.168.250.27':      # подсчет трафика, затраченного на отправку и на получение пакетов
            traffic += int(row[12])                                      # Данные для составления графика зависимости объема трафика от времени
            if time == row[0]:
                by += int(row[12])
            else:
                datalist += [[time, by]]
                time = row[0]
                by += int(row[12])

bill = (traffic) / (2 ** 20) * tarif # тарификация

with open('bill.txt', 'w') as out:          # выставление счета - запись в файл
    out.write('Bill for IP 192.168.250.27\n')
    out.write('Used Mb: ')
    out.write(str(round((traffic) / (2 ** 20), 2)))
    out.write('\nThe total bill: ')
    out.write(str(round(bill, 2)))
    out.write(' roubles')

del datalist[0]     # преобразование данных для построения графика
del datalist[0]
x = []
y = []
for i in range(len(datalist)):
    x += [datalist[i][0]]
    y += [datalist[i][1] / 1024]

figure()        # построение граффика
plot(x, y, 'r')
xlabel('time')
ylabel('traffic, Kb')
title('traffic(time)')
show()
