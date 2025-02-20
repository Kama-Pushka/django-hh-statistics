# Веб-приложение о профессии C# разработчик на Django
```
Репозиторий с исходным кодом сайта djangohhstatistics.pythonanywhere.com
```
Сайт предоставляет вводную информацию о профессии C# разработчика, а также различные аналитические данные о состоянии рынка труда в целом и рынке C# разработчиков в частности.

Анализ проводился на основе более чем 6 миллионов вакансий с сайта hh.ru за период с 2003 по 2024 год.
Основные разделы аналитики:

- Динамика развития трудового рынка (количество вакансий, уровень зарплат по годам и городам СНГ).
- Востребованность и география профессии C# разработчика.
- Изменение востребованности навыков с течением времени.

Все данные представлены в виде графиков и таблиц.

На сайте также доступна актуальная информация о последних вакансиях на позицию C# разработчика за последние сутки с портала hh.ru.

## Установка и запуск

- Создайте виртуальное окружение ```python -m venv hh_statistics\venv``` и перейдите в директорию hh_statistics ```cd hh_statistics```. 
- Активируйте окружение ```venv\scripts\activate```. 
- Установите зависимости ```pip install -r requirements.txt```.
- Создайте базу данных, аккаунт администратора и запустите сервер:
```
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
```

Через админку вы можете загрузить необходимый материал на страницы сайта. Исходные материалы лежат в папке ```data/```. 
