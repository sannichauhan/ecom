# 🛒 Django Stripe Store (48-Hour Assignment)

A modern, single-page e-commerce application built with Django and Stripe. This project demonstrates secure payment integration, state management, and clean UI design.

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone git@github.com:sannichauhan/ecom.git
cd ecom
```
### 2. Environment Setup

Create a `.env` file in the root directory `(refer to .env.example)`:
```text
STRIPE_PUBLIC_KEY=pk_test_your_public_key
STRIPE_SECRET_KEY=sk_test_your_private_key
DATABASE_NAME=your_db_name
DATABASE_USER=your_user
DATABASE_PASSWORD=your_password
```

### 3. Install Dependancy

```text
python -m venv env
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Database Initialization
```text
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
---
Note: 
- Log into /admin to add the 3 initial products with prices in Paise (e.g., 50000 for ₹500).
- Add 3 product initially into database logic written in apps.py when its ready.
---