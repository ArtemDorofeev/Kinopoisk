# Kinopoisk
Проект по анализу фильмов Кинопоиск.ru
=======
### Привет! Решил вылить все фильмы и сериалы лет так за 10 с Кинопоиска, как следует отанализировать и посмотреть, что получится))

### 1) Первичный сбор данных
  - Парсинг ссылок на фильм с разбивкой по годам (/Parse/Kinopoisk_parse_links)
  - Парсинг характеристик фильмов по ссылкам из объединенного датасета (/Parse/Kinopoisk_parse_char)
  - Организация промежуточного хранения данных парсинга в CSV (/CSV/characteristics)
  
### 2) Подготовка данных
  - Трансформация сырых данных в чистый датасет (/Transform/Transform_data.ipynb)
  - Организация хранения трансформированных данных в базе данных СУБД PostgreSQL
  
### 3) Разведочный анализ данных
  - Графический анализ числовых и категориальных данных (/EDA/EDA_kinopoisk.ipynb)
  
