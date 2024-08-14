def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    prov = ['.com', '.ru', '.net']
    s0 = False
    s1 = False

    for i in range(len(prov)):
        if ((recipient.find('@') != -1) and (recipient.find(prov[i]) != -1)):
            s0 = True
            break
        else:
            s0 = False


    if s0 == True:
        for i in range(len(prov)):
            if (sender.find('@') != -1) and (sender.find(prov[i]) != -1):
                s1 = True
                break
            else:
                s1 = False


    if s0 == False or s1 == False:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
    elif recipient.lower() == sender.lower():
        print("Нельзя отправить письмо самому себе!")
    elif sender.lower() == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес ", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')