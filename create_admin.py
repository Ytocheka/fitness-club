import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_club.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Найти первого пользователя и сделать его админом
user = User.objects.first()
if user:
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f'✅ Пользователь {user.email} стал администратором!')
else:
    print('❌ Нет пользователей в базе')