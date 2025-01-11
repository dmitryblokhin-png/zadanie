letter = """\
From: {0}
To: {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8";
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".replace("%website%","https://dvmn.org/profession-ref-program/ne_dmtr/p4Btx/").replace("%friend_name%","Мария Патока").replace("%my_name%","Дмитрий Блохин").format("samoshin2024@mail.ru", "mari@yandex.ru", "Приглашение")
my_site = "https://dvmn.org/profession-ref-program/ne_dmtr/p4Btx/"
my_friend = "Мария Патока"
my_name = "Дмитрий Блохин"
letter = letter.encode("UTF-8")
print(letter)
import smtplib
server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login('samoshin2024','hvcBCrTV9Jz1pAEkthxt')
server.sendmail('samoshin2024@mail.ru','maria.mzhavanadze@yandex.ru',letter)
server.quit()

