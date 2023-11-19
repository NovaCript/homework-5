Установите зависимости из requirements.txt.

pip install -r requirements.txt


Запуск прилодения файлом service.py



Откройте Postman для работы с приложением.

Для получения списка книг:
GET http://127.0.0.1:5000/books

Для получения конкретной книги по id:
GET http://127.0.0.1:5000/books/(значениеid)

Для обновленич книги:
PUT https://127.0.0.1:5000/books/(значениеid)

В теле запроса такие же параметры и пример запроса что и при создании книги ниже:

Для добавления книг:
POST http://127.0.0.1:5000/books

В теле запроса выберете raw - JSON формат.

Пример запроса:

{
    "title":"book5",
    "description":"easy description",
    "publish_year":2023,
    "pages_count":5
}

Для удаления книги:
DELETE http://127.0.0.1:5000/books/(значениеid)
