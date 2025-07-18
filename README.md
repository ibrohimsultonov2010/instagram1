# Instagram Login Clone

Instagram login sahifasining kloni Django bilan yaratilgan.

## O'rnatish

### 1. Kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 2. Migratsiyalarni ishga tushirish
```bash
python manage.py migrate
```

### 3. Superuser yaratish
```bash
python manage.py createsuperuser
```

### 4. Static fayllarni to'plash
```bash
python manage.py collectstatic
```

### 5. Serverni ishga tushirish
```bash
python manage.py runserver
```

## Funksiyalar

- Instagram login sahifasi kloni
- Foydalanuvchi ma'lumotlarini saqlash
- Admin panel orqali video URL ni o'zgartirish
- Instagram reels video ko'rsatish
- SEO optimizatsiyasi

## Admin Panel

- URL: `/admin/`
- Foydalanuvchi ma'lumotlarini ko'rish
- Video sozlamalarini o'zgartirish

## Fayllar tuzilishi

```
instagram/
├── app/
│   ├── templates/
│   │   └── instagram_login.html
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── project/
│   ├── settings.py
│   └── urls.py
├── requirements.txt
├── wsgi.py
└── manage.py
```

## PythonAnywhere ga o'rnatish

### 1. Fayllarni yuklang
- Barcha fayllarni PythonAnywhere ga yuklang

### 2. Konsol da ishlatish
```bash
# Kutubxonalarni o'rnatish
pip install -r requirements.txt

# Migratsiyalarni ishga tushirish
python manage.py migrate

# Superuser yaratish
python manage.py createsuperuser

# Static fayllarni to'plash
python manage.py collectstatic
```

### 3. Web app sozlash
- Web tab ga o'ting
- Source code: `/home/yourusername/instagram`
- Working directory: `/home/yourusername/instagram`
- WSGI configuration file ni oching va quyidagini yozing:

```python
import os
import sys

path = '/home/yourusername/instagram'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 4. Reload qilish
- "Reload" tugmasini bosing

### 5. Xatoliklar
Agar xatolik bo'lsa:
- Error log ni tekshiring
- `yourusername.pythonanywhere.com` ni `ALLOWED_HOSTS` ga qo'shing
- Database faylini tekshiring 