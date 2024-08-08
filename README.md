# Для работы с проектом должен быть установлен Docker

### Для работы заполните файл [.env.exampl](.env.exampl) затем переименуйте его в [.env](.envs)

### django_secret_key
- SECRET_KEY= секретный ключ от приложения джанго

### debug
- DEBUG= режим отладки включен или выключен булево значение

### db_password
- POSTGRES_DB= имя вашей БД
- POSTGRES_USER= пользователь БД
- POSTGRES_PASSWORD= пароль от БД
- POSTGRES_HOST= хост
- POSTGRES_PORT= порт
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

### Перед запуском приложения выполните команду в терминале
- docker compose up -d --build
-  или
- sudo docker compose -d --build

### Далее в браузере введите адрес
- http://0.0.0.0:8000/redoc/
- выйдет документация приложения

### есть функционал отправки уведомления об обновление подписках на курс пользователям
- создать аккаунт на сайте https://360.yandex.ru/mail/ если еще не создан
- в настройках https://mail.yandex.ru/?uid=1981646477#setup/client включить галочку на "С сервера imap.yandex.ru по протоколу IMAP"
- настроить аккаунт для писем зарегистрировать пароль для почты https://id.yandex.ru/security/app-passwords и сохранить его в файл .env

### Для выхода с сервера нажмите комбинацию клавиш в терминале
- ctrl+c