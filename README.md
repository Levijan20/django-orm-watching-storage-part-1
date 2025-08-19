
# 🏦 Пульт охраны банка
```
Внутренняя система мониторинга сотрудников банка «Сияние» с подключением к базе данных пропусков и визитов.
```
## 🚀 Быстрый старт

### 1. Клонирование и настройка
```bash
git clone <your-repo-url>
cd pulyt-ohrany-banka
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка базы данных
```bash
# Для PostgreSQL
sudo -u postgres psql -c "CREATE DATABASE bank_security;"
sudo -u postgres psql -c "CREATE USER security_user WITH PASSWORD 'secure_password123';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE bank_security TO security_user;"
```

### 4. Создание файла настроек
```bash
cat > .env << EOL
DB_ENGINE=django.db.backends.postgresql
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bank_security
DB_USER=security_user
DB_PASSWORD=secure_password123
SECRET_KEY=django-insecure-$(openssl rand -hex 32)
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EOL
```

### 5. Применение миграций
```bash
python manage.py migrate
```

### 6. Запуск тестового скрипта
```bash
python main.py
```

### 7. Проверка результата ✅

Если установка прошла успешно, вы увидите:
```
Количество пропусков: X
<QuerySet [<Passcard: Passcard object (1)>, <Passcard: Passcard object (2)>, ...]>
Всего активных пропусков: Y
```

Где X и Y - числа больше 0.

## 🔧 Если возникли проблемы

### Проверка подключения к БД
```bash
python -c "
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from django.db import connection
try:
    connection.ensure_connection()
    print('✅ Подключение к БД успешно')
except Exception as e:
    print(f'❌ Ошибка подключения: {e}')
"
```

### Проверка миграций
```bash
python manage.py showmigrations
```

### Сброс и повторная настройка
```bash
# Остановите сервер БД если запущен
sudo systemctl stop postgresql

# Удалите и создайте БД заново
sudo -u postgres psql -c "DROP DATABASE IF EXISTS bank_security;"
sudo -u postgres psql -c "CREATE DATABASE bank_security;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE bank_security TO security_user;"

# Повторно примените миграции
python manage.py migrate
```

## 📦 Требования

- Python 3.8+
- PostgreSQL 12+
- pip 20+

## 🐳 Docker альтернатива

```bash
# Установите Docker и Docker Compose
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Запустите полный стек
docker-compose up -d

# Проверьте работу
docker-compose logs app
```
