def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if ('@' not in sender or not sender.endswith(('.com', '.ru', '.net'))
            or '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net'))):
        print(f'Не возможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasia@gmail.com')
send_email('Это сообщение для проверки связи', 'vasia@mail.ru')
send_email('Это сообщение для проверки связи', 'vasia@beer.net')
send_email('Это сообщение для проверки связи', 'vasia@gmail.co')
send_email('Это сообщение для проверки связи', 'vasiamail.ru')
send_email('Это сообщение для проверки связи', 'vasiabeer.ne')
send_email('Это сообщение для проверки связи', 'vasia@mail.ru',sender='urban.info@gmail.com')
send_email('Это сообщение для проверки связи', 'university.help@gmail.com')
