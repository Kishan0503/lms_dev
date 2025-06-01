
# Library Management System — APIs

A RESTful API built with Django and Django REST Framework (DRF) to manage books, authors, genres, borrowing requests, and book reviews for students and librarians.

---

## Features

- JWT Authentication (Register, Login, Logout)
- Role-based access: **Student** & **Librarian**
- Book, Author, and Genre CRUD
- Borrow request flow: Pending → Approved/Rejected → Returned
- Book reviews with 1–5 star rating
- Signals for auto-updating book inventory
- Email notifications on borrow approval/rejection
- Search, Filter, and Ordering
- Swagger UI Documentation

---

## Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SimpleJWT (JWT Authentication)
- drf-yasg (Swagger UI)
- SQLite
- Django Filters

---

## Project Structure

```
library_management/
├── library/ (Book, BookReview, BorrowRequest models, views, signals, serializers)
├── user/    (CustomUser, Author, Genre models, views, serializers, auth, permissions)
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Kishan0503/lms_dev.git
   cd library_management
   ```

2. **Create virtual environment**  
   ```bash
   python -m venv venv
   venv\Scripts\activate  # or `source venv/bin/activate` on Linux
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Run server**  
   ```bash
   python manage.py runserver
   ```

---

## Authentication Endpoints

POST: `/api/register/` (Register new user)
POST: `/api/token/`    (Authenticate user with username and password and returns access and refresh token)
POST: `/api/token/refresh/` (Take refresh token and returns access token for login user)
POST: `/api/logout/`   (Logout user (blacklist token))

> Sample User Credentials:
# Student User

username: Student_User
email: student_user@gmail.com
password: student@123
role: STUDENT

# Librarian User

username: Librarian_User
email: librarian_user@gmail.com
password: librarian@123
role: LIBRARIAN

# Custom Permissions

IsLibrarianRequired : For users with role `LIBRARIAN`
IsStudentRequired : For users with role `STUDENT`

---

## Author and Genre API Endpoints
GET  :  `/api/authors/`  (Authenticated, List authors)
POST :  `/api/authors/`  (Librarian, Add authors)

GET  :  `/api/genres/`  (Authenticated, List genres)
POST :  `/api/genres/`  (Librarian, Add genres)


---

## Book API Endpoints

GET   :  `/api/books/`       (Authenticated, List books with filters)
GET   :  `/api/books/<id>/`  (Authenticated, Book details)
POST  :  `/api/books/`       (Librarian, Add book)   
PUT   :  `/api/books/<id>/`  (Librarian, Edit book)   
DELETE:  `/api/books/<id>/`  (Librarian, Delete book)   

> Filters: `?author=<id>&genres=<id>&search=title`

---

## Borrow Request API Endpoints

POST : `/api/borrow/`                  (Student, Request to borrow book)  
GET  : `/api/borrow/user/`             (Student, List own requests)  
PATCH: `/api/borrow/<id>/approve/`     (Librarian, Approve request)
PATCH: `/api/borrow/<id>/reject/`      (Librarian, Reject request)
PATCH: `/api/borrow/<id>/return/`      (Librarian, Mark as returned)

---

## Book Review API Endpoints

GET :    `/api/books/<id>/reviews/`     (Authenticated, List reviews for book) 
POST :   `/api/books/<id>/reviews/`     (Authenticated, Add review (1–5 rating))

---

## Email Notifications

Students are notified via email when:
- Borrow requests are **approved**
- Borrow requests are **rejected**

---

## API Docs

Swagger UI is available at:

```
http://127.0.0.1:8000/swagger/
```