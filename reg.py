import requests

#словарь для майла и пароля
slovar = {
    'email':'def',
    'username':'def',
    'password':'def',
    'password':'def',
    #'password':'def',
    #'password':'def',
       }
#Ввод данных
log = input("Введите майл: ")
pas = input("Введите password: ")


#переносим данные в словарь
slovar['email'] = log
slovar['password'] = pas

#ссылка на сайт регистрация
url = 'https://discord.com/register'
#url = 'https://discord.com/login'

#создаем сессию
sosok = requests.Session()

#отправляем запрос
lo = sosok.post(url, data = slovar)

#cохраняем данные
#открываем файл
file = open('result.txt', 'w+')

#записываем
file.write(lo.text)

#закрываем файл
file.close()
