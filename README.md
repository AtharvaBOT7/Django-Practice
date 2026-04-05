# Django Practice 🐍

A beginner Django project built while following a YouTube tutorial. This repo documents my learning journey with Django from scratch.
YT Link - https://m.youtube.com/watch?v=3gpo9piG12E&pp=ygUdZGphbmdvIHR1dG9yaWFsIGZvciBiZWdpbm5lcnM%3D

---

## 📚 What I Learned

### Core Concepts
- What Django is and why we use frameworks over writing everything from scratch
- Django's **MVT architecture** (Model, View, Template) and how data flows between them
- Breaking down `settings.py` — `BASE_DIR`, `SECRET_KEY`, `DEBUG`, `INSTALLED_APPS`, `MIDDLEWARE`, `DATABASES`, `STATIC_URL` and more

### Project Setup
- Creating a Django project using `django-admin startproject mysite .`
- Running the dev server with `python manage.py runserver`
- Understanding the role of each default file — `manage.py`, `urls.py`, `wsgi.py`, `settings.py`

### Templates & Static Files
- Setting up a `templates/` folder and rendering HTML using `render(request, 'home.html')`
- Loading static files (CSS, images) using `{% load static %}` and configuring `STATIC_ROOT` and `STATICFILES_DIRS` in `settings.py`
- Adding Bootstrap via CDN for quick responsive styling

### Django Apps
- Creating a separate app using `python manage.py startapp employees`
- Understanding why apps are used to keep features modular and maintainable
- Registering the app in `INSTALLED_APPS` inside `settings.py`

### Models & Migrations
- Defining database models in `models.py` by inheriting from `models.Model`
- Running `makemigrations` and `migrate` to create database tables
- Configuring media file uploads using `MEDIA_ROOT` and `MEDIA_URL`

### Admin Panel
- Creating a superuser with `python manage.py createsuperuser`
- Registering models in `admin.py` to manage records via the built-in admin panel

### Views & URLs
- Writing view functions and mapping them to URLs using `path()` in `urls.py`
- Using `include()` to connect app-level URLs to the project-level `urls.py`
- Passing data to templates using a `context` dictionary
- Dynamic URLs using `<int:pk>` and fetching records with `get_object_or_404()`

### Template Tags
- Using `{% for %}` loops to display database records in HTML tables
- Using `{{ forloop.counter }}` for row numbering
- Using `{% url 'name' %}` for named URL routing

---

## 🛠️ Tech Stack
- Python 3.12
- Django
- SQLite (default)
- Bootstrap 5 (CDN)

---

## ⚙️ Setup
```bash
# Clone the repo
git clone <your-repo-url>
cd Django-Practice

# Activate virtual environment
source djangopractice/bin/activate

# Install dependencies
pip install django pillow

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

---

## 📝 Notes
This project is purely for learning purposes. All employee records used are dummy data.