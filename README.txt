'http://127.0.0.1:8000/scrap/new/<str:name>'-Scrap information about new company name
'http://127.0.0.1:8000/scrap/one/<str:name>'-represent information from database about chosen company
'http://127.0.0.1:8000/scrap/update/'-update information in database(include real time information, not only yesterday)
'http://127.0.0.1:8000/scrap/'- represent all database information


Для цього проекту корисно було використати Celery для фонового виконання задач, таких як оновлення чи додавання нової інформації
також щоденне автоматичне оновлення бази данних, в мене нажаль виникли з цим проблеми тому я не став додавати
це до фінального релізу. Якщо буде потрібно я представлю проект з Celery.