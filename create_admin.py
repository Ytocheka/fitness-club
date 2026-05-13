import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_club.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(email='admin@gmail.com').exists():
    admin = User.objects.create_superuser(
        email='admin@gmail.com',
        full_name='Администратор',
        phone='+79991234567',
        birth_date='1990-01-01',
        password='12345678'
    )
    print('✅ Суперпользователь создан!')
    print('Email: admin@fitnessclub.ru')
    print('Пароль: admin123456')
else:
    print('❌ Пользователь уже существует')