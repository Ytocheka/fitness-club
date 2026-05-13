#!/usr/bin/env bash
# exit on error
set -o errexit

# Установка зависимостей
pip install -r requirements.txt

# Сбор статических файлов
python manage.py collectstatic --no-input

# Применение миграций (ДО создания админа!)
python manage.py migrate

# Создание администратора (ПОСЛЕ миграций!)
python manage.py shell < create_admin.py