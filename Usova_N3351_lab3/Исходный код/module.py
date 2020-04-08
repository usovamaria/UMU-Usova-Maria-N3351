# Лабораторная 3
# Вариант 18 (3)

from fpdf import *

bankname = 'Банк Санкт-Петербург'       # Данные для заполнения полей формы
bankbink = '044030790'
bankinn = '7831000027'
bankkpp = '783501001'
name = 'Усова Мария Андреевна'
cash = '30101810900000000790'
cashnum = '3351'
date = '08.04.2020'
postav = 'ООО Питер-Телеком'
zakaz = 'Усова Мария Андреевна'
zvonok = 16.23
zvonok_price = 2
zvonok_total = zvonok_price * zvonok
sms = 15
sms_cost = 2
sms_total = sms * sms_cost
internet = 3.62
internet_cost = 1
internet_total = internet * internet_cost
bill = internet_total + zvonok_total + sms_total
sum = 'Шестьдесят шесть рублей восемь копеек'
writing1 = 'Внимание!'
writing2 = 'Оплата данного счета означает согласие с условиями поставки товара. Уведомление об оплате обязательно.'
writing3 = 'Оказание услуги производится по факту прихода денег на расчетный счет Поставщика.'

def filling(spacing = 2):
    data = [['Банк получателя  ' + bankname, 'БИК   ' + bankbink],      # Данные расчетных счетов
            ['ИНН   ' + bankinn, 'КПП   ' + bankkpp],
            ['Получатель   ' + name, 'Счет  ' + cash]]
    tovar = [['№', 'Товары (работы, услуги)', 'Кол-во', 'Ед.', 'Цена', 'Сумма'],        # Данные для таблицы услуг
             ['1', 'Услуга "Звонки"', str(zvonok), 'мин', str(zvonok_price) + ' руб/мин', str(zvonok_total)],
             ['2', 'Услуга "СМС"', str(sms), 'шт', str(sms_cost) + ' за шт', str(sms_total)],
             ['3', 'Услуга "Интернет"', str(internet), 'Мб', str(internet_cost) + 'за Мб', str(internet_total)]
            ]
    low = ['Товары (работы, услуги)', 'Услуга "Звонки"', 'Услуга "СМС"', 'Услуга "Интернет"'] # Для расширенного поля в таблице
    pdf = FPDF()    # Создание PDF и установка шрифта, поддерживающего кодировку UTF-8
    pdf.add_page()
    pdf.add_font('FreeSans', '', 'FreeSans.ttf', uni=True)
    pdf.set_font("FreeSans")

    col_width = pdf.w / 2.5
    row_height = pdf.font_size

    for row in data:        # Создание таблицы с расчетным счетом
        for item in row:
            pdf.cell(col_width, row_height * spacing, txt = item, border = 1)
        pdf.ln(row_height * spacing)

    pdf.set_font_size(size=20)      # Запись информации о номере счета, поставщике и покупателе
    pdf.cell(ln = 5, h = 20, align = 'L', w = 0, txt = 'Счет на оплату №' + cashnum + ' от ' + date, border = 0)
    pdf.set_font_size(size=12)
    pdf.cell(ln = 5, h = 10, align = 'L', w = 0, txt = 'Поставщик (Исполнитель):   ' + postav, border = 0)
    pdf.cell(ln = 5, h = 10, align = 'L', w = 0, txt = 'Покупатель (Заказчик):   ' + zakaz, border = 0)
    pdf.cell(ln = 5, h = 10, align = 'L', w = 0, txt = 'Основание:   ', border = 0)

    col_width = pdf.w / 9
    for row in tovar:       # Создание и заполнение таблицы с данными о товарах
        for item in row:
            if item in low:
                pdf.cell(col_width * 2.5, row_height * spacing, txt = item, border = 1)
            else:
                pdf.cell(col_width, row_height * spacing, txt = item, border = 1)
        pdf.ln(row_height * spacing)
        
    # Запись полей "Итого" и всей последующей информации
    pdf.cell(ln = 5, h = 20, align = 'R', w = 150, txt = 'Итого:   ' + str(bill), border = 0)
    pdf.cell(ln = 5, h = 0, align = 'R', w = 150, txt = 'Всего к оплате:   ' + str(bill), border = 0)
    pdf.set_font_size(size = 9)
    pdf.cell(ln = 5, h = 5, align = 'L', w = 0, txt = 'Всего наименований: 3,', border = 0)
    pdf.cell(ln = 5, h = 10, align = 'L', w = 0, txt = 'Сумма прописью: ' + sum, border = 0)
    pdf.cell(ln = 5, h = 5, align = 'L', w = 0, txt = writing1, border = 0)
    pdf.cell(ln = 5, h = 5, align = 'L', w = 0, txt = writing2, border = 0)
    pdf.cell(ln = 5, h = 5, align = 'L', w = 0, txt = writing3, border = 0)

    # Линия-разделитель и место для подписей
    pdf.line(10, 175, 200, 175)
    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)
    pdf.cell(ln = 5, h = 25, align = 'L', w = 0, txt = 'Руководитель  ' + '_' * 30 + '  Бухгалтер ' + '_' * 30, border = 0)

    pdf.output('bill.pdf')

if __name__ == '__main__':
    filling()
