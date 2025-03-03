# FastAPI + MariaDB + MVC Project 🚀

This is a FastAPI project using MariaDB with the MVC pattern and JWT authentication.

## 📌 Features
- **FastAPI** for the backend.
- **MariaDB** as the database.
- **JWT Authentication** for user login & security.
- **MVC Pattern** for structured code organization.
- **Docker Support** for easy deployment.

## 🛠️ Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/fastapi-mariadb-mvc.git
cd fastapi-mariadb-mvc
```

### **2. Set Up Virtual Environment (Optional)**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up `.env` File**
Copy `.env.example` to `.env` and fill in your database credentials.
```bash
cp .env.example .env
```

### **5. Run the Application**
#### Using Uvicorn:
```bash
uvicorn app.main:app --reload
```

#### Using Docker:
```bash
docker-compose up --build
```

---

## 🐳 Docker Installation and Setup

### **1. Install Docker**
Download and install Docker from [here](https://www.docker.com/get-started/).

### **2. Build and Run the Docker Container**
```bash
docker-compose up --build
```

### **3. Stop the Containers**
```bash
docker-compose down
```

### **4. Rebuild Without Cache**
```bash
docker-compose build --no-cache
```

---

## 🛠️ API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login & get JWT token |
| GET | `/products/` | Get all your products |
| POST | `/products/` | Create a product |
| PUT | `/products/{id}` | Update your product |
| DELETE | `/products/{id}` | Delete your product |

---

## 🎯 Project Structure

```
📂 app
 ┣ 📂 controllers    # Handles business logic
 ┣ 📂 models         # Database models
 ┣ 📂 routes         # API endpoints
 ┣ 📂 services       # Business logic (auth, etc.)
 ┣ 📂 utils          # Helper functions (JWT, hashing)
 ┣ 📜 main.py        # FastAPI entry point
 ┗ 📜 database.py    # Database setup
```



