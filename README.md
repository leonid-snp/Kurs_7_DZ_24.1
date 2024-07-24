# Для работы с проектом необходимо установить все завсимости в файле [pyproject.toml](pyproject.toml)

### Перед запуском приложения примените все миграции командой
- python3 manage.py migrate

### Выполни команду в консоли для тестового заполнения баз-данных
- python3 manage.py loaddata db.json

### Для работы заполните файл [.env.exampl](.env.exampl) затем переименуйте его в [.env](.envs)

### django_secret_key
- SECRET_KEY= секретный ключ от приложения джанго

### debug
- DEBUG= режим отладки включен или выключен булево значение

### db_password
- NAME= имя вашей БД
- USER_BD= пользователь БД
- PASSWORD= пароль от БД
- HOST= хост
- PORT= порт
- 
### stripe_api_key
- STRIPE_API_KEY=апи ключ для сервиса платежей stripe

### celery_setting
- CELERY_BROKER_URL=порт для брокера
- CELERY_RESULT_BACKEND=порт для бекенда
- CELERY_CACHE_BACKEND=порт для кеша
- CELERY_TASK_TRACK_STARTED=булево значение

### email_password
- EMAIL_HOST=хост сервиса отправки писем
- EMAIL_PORT=порт
- EMAIL_USE_TLS=использовать безопасное соединение, булево значение
- EMAIL_USE_SSL=использовать защищенное соединение, булево значение
- EMAIL_HOST_USER=логин от сервиса отправки писем
- EMAIL_TO=почта с которой будут отправляться письма
- EMAIL_HOST_PASSWORD=пароль от приложения отправки писем

### есть функционал отправки уведомления об обновление подписках на курс пользователям
- создать аккаунт на сайте https://360.yandex.ru/mail/ если еще не создан
- в настройках https://mail.yandex.ru/?uid=1981646477#setup/client включить галочку на "С сервера imap.yandex.ru по протоколу IMAP"
- настроить аккаунт для писем зарегистрировать пароль для почты https://id.yandex.ru/security/app-passwords и сохранить его в файл .env

### Чтобы запустить приложение в консоли введите команду
- python manage.py runserver

### Перейдите по ссылке в терминале где написано 
- Starting development server at http://127.0.0.1:8000/

### Для выхода с сервера нажмите комбинацию клавиш в терминале
- ctrl+c