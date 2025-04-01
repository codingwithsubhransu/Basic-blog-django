# 📝 Basic Blog API - Django REST Framework + JWT Authentication

This repository contains a **Blog API** built using **Django REST Framework (DRF)** and **Simple JWT Authentication**. It is designed to **learn CRUD operations** and implement authentication features.

---

## 🚀 Features
✅ **Public Access**: Anyone can view all blog posts.  
✅ **JWT Authentication**: Users must log in to manage their posts.  
✅ **User-Specific Actions**: Only the **author** of a blog post can delete it.  
✅ **Secure API**: Uses **token-based authentication** with JWT.  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```
git clone https://github.com/codingwithsubhransu/Basic-blog-django.git
cd Basic-blog-django
```

### 2️⃣ Create a Virtual Environment
```
python -m venv venv
# On macOS/Linux
source venv/bin/activate  
# On Windows
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```
python manage.py migrate
```

### 5️⃣ Create a Superuser (Optional)
```
python manage.py createsuperuser
```

### 6️⃣ Run the Server
```
python manage.py runserver
```

---

## 🛠️ API Endpoints

### 🔹 Authentication
| Method | Endpoint            | Description                      |
|--------|---------------------|----------------------------------|
| POST   | `/api/v1/register/` | Register a new user             |
| POST   | `/api/v1/login/`    | Get an access + refresh token   |
| POST   | `/api/v1/logout/`   | Logout and blacklist token      |

### 🔹 Blog Posts
| Method  | Endpoint                  | Description                      | Access        |
|---------|---------------------------|----------------------------------|--------------|
| GET     | `/api/v1/blogs/`          | Get all blog posts               | Public       |
| DELETE  | `/api/v1/blogs/{id}/delete/` | Delete a blog (only author)     | Authenticated |

---

## 🔑 Authentication  
This project uses **JWT Authentication**.  
After logging in, include the **access token** in the headers:

```
Authorization: Bearer your_access_token
```

To get a new **access token**, send a POST request:
```
curl -X POST http://127.0.0.1:8000/api/v1/login/ -d "username=user&password=pass"
```

---

## 📜 License  
This project is open-source and available under the **MIT License**.

---

## 📧 Contact  
👤 **Subhransu Sekhar Rout**  
📧 Email: subhransusekharrout987@gmail.com  
🔗 GitHub: [codingwithsubhransu](https://github.com/codingwithsubhransu)  
