# Flat Project

## 📌 Описание

Этот проект демонстрирует работу с **итераторами** и **генераторами** в языке Python.  
Реализованы:

- Классический итератор `FlatIterator`, разворачивающий вложенные списки
- Генераторная функция `flat_generator` с тем же функционалом
- Юнит-тесты к ним с использованием библиотеки `pytest` и параметризации

## 📂 Структура проекта

flat_project/ ├── flat_iterator.py # Класс FlatIterator ├── flat_generator.py # Функция flat_generator ├── test_flat_iterator.py # Тесты для FlatIterator (pytest) ├── test_flat_generator.py # Тесты для flat_generator (pytest)


## 🚀 Запуск тестов

Убедитесь, что установлен `pytest`:

```bash
pip install pytest

Затем в терминале в корне проекта выполните:
pytest
Или запустите конкретный файл:
pytest test_flat_iterator.py
pytest test_flat_generator.py

Пример использования

# Использование FlatIterator
nested_list = [[1, 2], [3, 4]]
for item in FlatIterator(nested_list):
    print(item)  # 1 2 3 4

# Использование flat_generator
for item in flat_generator(nested_list):
    print(item)  # 1 2 3 4
    
Автор
Проект выполнен в рамках учебного задания по теме "Итераторы, генераторы, тестирование".