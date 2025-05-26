## 🏛️ Library Management System Using Django

A web-based library management system built with Django. This project allows administrators to manage books and users to view available books. It includes features such as adding, deleting, and viewing books, as well as a RESTful API integration.

---

## 📁 Project Structure

Directory structure:

    ├── README.md
    ├── LICENSE
    ├── manage.py
    ├── api/
    │   ├── __init__.py
    │   ├── serializers.py
    │   ├── urls.py
    │   └── __pycache__/
    ├── library/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── __pycache__/
    │   └── migrations/
    │       ├── 0001_initial.py
    │       ├── 0002_author_book_delete_item.py
    │       ├── 0003_remove_book_author_delete_author.py
    │       ├── __init__.py
    │       └── __pycache__/
    └── Library_Management/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        └── __pycache__/

---


## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/shravaniraut175/library-management-system.git
cd library-management-system
```

### 2. Create a Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install django djangorestframework
```

### 4. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```
python manage.py runserver
```
Then open your browser and go to:
📍 http://127.0.0.1:8000/

---

## 📚 Features
✅ Add and Delete Books (Admin)

✅ View Available Books

✅ REST API Support via Django REST Framework

✅ Admin Panel Integration

✅ Modular App Structure with Models, Views, and Serializers

--- 

## 🧠 How It Works
Models: Defines the structure of the database with fields for books and any related entities.

Admin Panel: Admin can log in via /admin to manage books directly.

Views: Handles logic for displaying books and processing API requests.

Serializers: Converts complex data (like model instances) into native Python datatypes for API responses.

URLs: Routes user and API requests to the appropriate views.

--- 

## 📄 Files to Check
File	                    | Description

views.py (library)	      | Core business logic for book-related operations

models.py (library)	      | Book model definition

serializers.py (api)	    | Handles API data conversion

urls.py (project & apps)	| URL routing for frontend and APIs

settings.py	              | App registration, middleware, and DB configuration


---

## 🧑‍💻 Author

Shravani

[GitHub Profile](https://github.com/shravaniraut175)

---

## 📄 License
This project is open source and available under the MIT License.

