# Finance Dashboard Backend

##  Overview

This project is a backend system for a finance dashboard that allows users to manage financial records with role-based access control and view summarized analytics.

The system is designed with a focus on clean API design, modular structure, and proper permission handling.

---

##  Features

### 👤 User & Role Management

* Custom user model
* Role-based access:

  * **Admin** → Full access (CRUD + user management)
  * **Analyst** → Read-only (records + dashboard)
  * **Viewer** → Dashboard access only

---

###  Financial Records

* Create, read, update, delete records
* Fields:

  * Amount
  * Type (Income / Expense)
  * Category
  * Date
  * Notes
* Filtering support:

  * By category
  * By type
  * By date range

---

###  Dashboard APIs

* Total income
* Total expenses
* Net balance

---

###  Access Control

* Implemented using custom permission class
* Enforces role-based restrictions:

  * Viewers cannot modify data
  * Analysts cannot create/update/delete
  * Admin has full control

---

###  Validation & Error Handling

* Serializer-based validation
* Proper HTTP status codes (400, 403, etc.)
* Handles invalid input and unauthorized access

---

##  Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

---

##  API Endpoints

### Records

* `GET /api/records/` → List records (with filters)
* `POST /api/records/` → Create record (Admin only)
* `PUT /api/records/{id}/` → Update record
* `DELETE /api/records/{id}/` → Delete record

### Dashboard

* `GET /api/dashboard/` → Summary data

---

##  Filtering Example

```bash
/api/records/?category=food&type=expense&start_date=2026-01-01&end_date=2026-04-01
```

---

##  Setup Instructions

```bash
git clone <repo-url>
cd finance_backend

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

##  Assumptions

* Roles are stored as a field in the User model
* SQLite is used for simplicity
* Authentication uses Django session login

---

##  Project Structure

* `users/` → User & role management
* `records/` → Financial records & APIs
* `dashboard/` → Summary APIs

---

##  Notes

* This project focuses on backend design and logic clarity rather than production deployment.
* Additional enhancements like JWT auth, pagination, and API docs can be added easily.

---
## Live Demo
Login:
https://finance-data-processing-and-access-tsoo.onrender.com/api-auth/login/?next=/api/records/

API:
https://finance-data-processing-and-access-tsoo.onrender.com/api/records/


## Demo Credentials
Username: areesh   (or admin)
Password: areesh@080902

##  How to Use Live Demo

1. Open the login link  
2. Enter demo credentials  
3. You will be redirected to the records API  
4. Use the browsable API to:
   - View records (GET)
   - Add records (POST)
   - Update/Delete (Admin only)


###  Pagination

* Implemented using DRF pagination
* Limits number of records per request