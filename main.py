import os
from django.db import models


import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


from datacenter.models import Passcard  # noqa: E402


if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001

from django.db import models

passcards = Passcard.objects.all()
print(passcards) 

passcard = Passcard.objects.first()  # взять первый пропуск из базы

active_passcards = []

active_passcards = Passcard.objects.filter(is_active=True)

print(f"Всего активных пропусков: {len(active_passcards)}")
