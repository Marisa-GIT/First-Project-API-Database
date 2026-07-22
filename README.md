# 🚀 API Data Validator & Testing Framework

A Python-based QA Automation project that combines **API Testing, Data Validation, Database Integration, and Backend Development**.

This project simulates a real-world QA workflow by consuming data from an external REST API, validating business rules, storing test results in a MySQL database, exposing an internal Flask API, and executing automated tests with **Pytest** and **Postman**.

---

## 📌 Features

- 🌐 Consume data from an external REST API
- ✅ Validate business rules
- 🗄️ Store users and test results in MySQL
- 🔗 Expose REST endpoints with Flask
- 🧪 Automated API testing with Pytest
- 📮 Manual API testing with Postman
- 📝 Logging and error handling
- 📊 Generate execution reports

---

## 🛠️ Tech Stack

- Python
- Flask
- MySQL
- Requests
- Pytest
- Postman
- Logging
- Git & GitHub

---

## 🎯 Project Workflow

The application performs the following steps:

1. Retrieves users from an external REST API.
2. Validates business rules for each user.
3. Stores user information in the database.
4. Stores validation results in a separate table.
5. Exposes an internal REST API to manage users.
6. Executes automated and manual API tests.

### Business Rules

Each user is validated according to the following rules:

- Email must contain **"@"**
- Username must contain **at least 5 characters**

Each validation is stored as **PASS** or **FAIL**.

---

# 📂 Project Structure

```text
API-Data-Validator/

├── api/
│   ├── external_api_testing/
│   │   └── get_users.py
│   │
│   ├── internal_api/
│   │   ├── __init__.py
│   │   └── app.py
│   │
│   ├── api_tests.py
│   └── __init__.py
│
├── database/
│   ├── db_connection.py
│   ├── insert_users.py
│   ├── schema.sql
│   └── __init__.py
│
├── validation/
│   ├── validator.py
│   └── __init__.py
│
├── tests/
│   ├── test_health.py
│   ├── test_main.py
│   ├── test_validation.py
│   └── __init__.py
│
├── postman/
│   ├── API Flask.postman_collection.json
│   └── API-jsonplaceholder.postman_collection.json
│
├── screenshots/
│
├── logs/
│   └── api_errors.log
│
├── conftest.py
├── pytest.ini
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git https://github.com/Marisa-GIT/First-Project-API-Database.git

cd First-Project-API-Database
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🗄️ Database Setup

Run the SQL script located in:

```text
database/schema.sql
```

This script creates all required tables.

---

# ▶️ Running the Project

## 1. Insert Users

```bash
python database/insert_users.py
```

---

## 2. Execute the Validation Workflow

```bash
python main.py
```

The application will:

- Retrieve users from the external API
- Validate business rules
- Execute API tests
- Store results in MySQL
- Display a summary report

Example:

```text
🌐 API TESTS

status_code      PASS
response_time    PASS
json_format      PASS

📊 TEST REPORT

Total: 23
PASS : 22
FAIL : 1
Success Rate: 95.65%
```

---

## 3. Run the Flask API

```bash
python -m api.internal_api.app
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

# 🔗 API Endpoints

| Method | Endpoint | Description |
|----------|----------------|---------------------------|
| GET | /users | Retrieve all users |
| POST | /users | Create a new user |
| PUT | /users/{id} | Update an existing user |
| DELETE | /users/{id} | Delete a user |
| GET | /health | Health check endpoint |

Example request:

```json
{
    "name": "Isabel",
    "email": "isabel@test.com",
    "username": "isabelqa"
}
```

---

# 🧪 Testing

## Pytest

Run all automated tests:

```bash
python -m pytest -v
```

Example output:

```text
=========================
4 passed in 2.48s
=========================
```

Current automated tests include:

- Health endpoint
- Main workflow
- User validation
- API endpoints

---

## Postman

The project includes two Postman collections:

- External API Testing
- Internal Flask API Testing

Validated scenarios:

- ✅ Status Codes
- ✅ Response Time
- ✅ JSON Schema
- ✅ CRUD Operations
- ✅ Field Validation

---

# 📸 Screenshots

## Postman

![Postman GET](screenshots/postmanGet.png)

![Postman Tests](screenshots/postmanTest.png)

---

## Console Report

![Console](screenshots/console.png)

---

## MySQL Database

### Users Table

![Users](screenshots/databaseUsers.png)

### Test Results Table

![Test Results](screenshots/databaseTest.png)

---

# 📈 Key Learning Outcomes

Through this project I practiced:

- REST API Testing
- Backend Development with Flask
- Business Rule Validation
- Database Integration with MySQL
- Automated Testing with Pytest
- Manual API Testing with Postman
- Error Handling and Logging
- Project Architecture and Modular Design

---

# 🚀 Future Improvements

- JWT Authentication
- Docker Support
- GitHub Actions CI/CD
- Swagger/OpenAPI Documentation
- Test Coverage Reports
- Performance Testing
- Environment Variables (.env)

---

# 👩‍💻 Author

**Isabel Vides**

Junior QA Automation Engineer

This project was developed as part of my QA Automation portfolio to demonstrate API testing, backend development, database integration, and automated testing skills.





