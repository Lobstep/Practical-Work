# Читаем файл, где имеются домены(mail, yandex, xakep, gmail)
f_read = open(u'users.txt', 'r', encoding='UTF-8').readlines()
# Создаём файл для mail
mail = open(u'email.txt', 'w', encoding='UTF-8')
# Создаём файл для yandex
yandex = open(u'yandex.txt', 'w', encoding='UTF-8')
# Создаём файл для xakep
xak = open(u'xak.txt', 'w', encoding='UTF-8')
# Создаём файл для остальных доменов, которые не подходят
rest = open('rest.txt', 'r', encoding='UTF-8').readlines()
print('Начинается сканирование!')
# Запускаем цикл, где перебираем строки из файла
for domain in f_read:
    # Ищем строки с @mail
    if '@mail' in domain:
        # Записываем их в файл
        with open('email.txt', 'a', encoding='UTF-8') as mail:
            mail.write(domain)
        # Ищем строки с @yandex
    elif '@yandex' in domain:
        with open('yandex.txt', 'a', encoding='UTF-8') as yandex:
            yandex.write(domain)
        # Ищем строки с @xakep
    elif '@xak' in domain:
        with open('xak.txt', 'a', encoding='UTF-8') as xak:
            xak.write(domain)
        # Записываем не найденные домены
    if '@xak' not in domain and '@mail' not in domain and '@yandex' not in domain:
        with open('rest.txt', 'a', encoding='UTF-8') as rest:
            rest.write(domain)
print('Сканирование завершено!')
