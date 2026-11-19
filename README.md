# 🚀 API Data Validator & Testing Framework

[![CI](https://github.com/Marisa-GIT/First-Project-API-Database/actions/workflows/tests.yml/badge.svg)](
https://github.com/Marisa-GIT/First-Project-API-Database/workflows/tests.yml
)

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

## 🎯 Project Objective

The goal of this project is to simulate a complete QA validation workflow:

- Retrieve data from an external API
- Apply business validation rules
- Store validation results in a database
- Expose an internal REST API
- Perform automated and manual API testing

---

### Validation Rules

For each user retrieved from the external API:

- Verify that the email contains @
- Verify that the username contains at least 5 characters
- Mark the user as valid or invalid
- Store validation results in MySQL
- Generate a testing report

Example validation failure:

username_length | FAIL |
Username 'Bret' has 4 characters. Minimum required: 5.


---

# 📂 Project Structure

```text
API-Data-Validator/
│
├── api/
│   ├── __init__.py
│   ├── api_tests.py
│   │
│   ├── external_api_testing/
│   │   ├── __init__.py
│   │   └── get_users.py
│   │
│   └── internal_api/
│       ├── __init__.py
│       └── app.py
│
├── database/
│   ├── __init__.py
│   ├── db_connection.py
│   ├── insert_users.py
│   └── schema.sql
│
├── validation/
│   ├── __init__.py
│   └── validator.py
│
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_main.py
│   └── test_validation.py
│
├── logs/
│   └── api_errors.log
│
├── postman/
│   ├── API Flask.postman_collection.json
│   └── API-jsonplaceholder.postman_collection.json
│
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── main.py
```
---

# 🛠 Technologies Used

Technology  	Purpose
Python	        Core development language
Flask	        Internal REST API
MySQL	        Database storage
Requests	    External API consumption
Pytest	        Automated testing
Postman	        API testing
Git & GitHub	Version control
Logging	        Error tracking

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

Verify that the required tables were created:

SHOW TABLES;

Expected:

users
test_results

----

# ▶️ Running the Project

## 1. Insert Users

```bash
python database/insert_users.py
```
---
Expected output:

Users inserted successfully

---
Execute validations:

python main.py

---

## 2. Execute the Validation Workflow

```bash
python main.py
```

This process:

- Retrieves users
- Runs API tests
- Validates business rules
- Stores results in MySQL
- Generates a summary report

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

- ✅ HTTP status codes
- ✅ Response Time
- ✅ JSON structure
- ✅ Data validation rules
- ✅ Expected fields

# 📊 Sample Report

🌐 API TESTS
status_code      PASS
response_time    PASS
json_format      PASS

📊 TEST REPORT

Total: 23
PASS: 22
FAIL: 1
Success Rate: 95.65%

❌ FAILED TESTS

User ID: 1
Test: username_length
Reason: Username 'Bret' has 4 characters. Minimum required: 5.

# 📝 Logging

Errors are stored in:

logs/api_errors.log

Example:

ERROR: Duplicate entry detected

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

# 🧪 Testing Architecture

The project demonstrates three testing layers:

- Unit Tests
- test_validation.py
- test_main.py
- Integration Tests
- MySQL database connectivity
- External API consumption
- API / End-to-End Tests
- Flask endpoints
- Postman collections

---

# 📈 Key Learning Outcomes

Through this project I practiced:

- REST API consumption
- Business rule validation
- MySQL integration
- Automated testing with Pytest
- API testing with Postman
- Flask API development
- Error handling and logging
- Modular Python architecture
- GitHub workflow integration

---

# 🚀 Future Improvements

- JWT Authentication
- Docker support
- Swagger/OpenAPI documentation
- Additional validation rules
- Increased test coverage

---

# 👩‍💻 Author

**Isabel Vides**

Junior QA Automation Engineer

This project was developed as part of my QA Automation portfolio to demonstrate API testing, backend development, database integration, and automated testing skills.





