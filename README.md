# Публикация комиксов в сообществе Вконтакте

Скрипт скачивает случайный комикс с [https://xkcd.com](https://xkcd.com/) и публикует его в сообществе Вконтакте

## Установка

- Создайте .env файл с переменными GROUP_ID и ACCESS_TOKEN
- Создайте сообщество вконтакте и поместите id группы в переменную GROUP_ID
- Создайте приложение на странице для разработчиков [https://vk.com/dev](https://vk.com/dev), тип приложения standalone
- Получите ключ доступа пользоователя [https://vk.com/dev/implicit_flow_user](https://vk.com/dev/implicit_flow_user) в параметре scope указывайте: photos, wall, groups и offline, после завершения процедуры в адресной строке появится значение access_token, поместите это значение в файл .env
- Установите зависимости командой:

	pip install -r requirements.txt

## Пример использования

    python main.py 

Результат:

![](https://dvmn.org/media/filer_public/93/e1/93e1ead6-bd6f-4cb2-a0ae-5ec036617f49/xkcd.gif)

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
