# QRkot_spreadseets
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/-Selenium-464646?style=flat-square&logo=Selenium)](https://www.selenium.dev)
[![openpyxl](https://img.shields.io/badge/-openpyxl-464646?style=flat-square&logo=openpyxl)](https://openpyxl.readthedocs.io/en/stable/)
Проект по парсингу сайта https://www.zara.com/kz/. Получение карточки товара и ее содержания, в категориях:
Жещины/рубашки и Мужчины/овершот

## Использование
Склонируйте репозиторий  
Создайте виртуальное окружение 
```
python -m venv venv
```
Активируйте виртуальное окружение
* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate

Установите зависимости 
```
pip install -r requirements.txt
```
Запустите проект
```
py main.py
```

Данная программа собирает данные в файл res.xlsx в формате:
Артикуль-Название-Цена-Описание-Ссылка.на.фото-Свойства-Дата.парсинга

## Над проектом работали
- [Дмитрий Луконин](https://wa.me/79153612056)