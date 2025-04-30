 # 🚗 AutoFleetCLI - Python CRUD Project

**AutoFleetCLI** is a simple, command-line-based car inventory management system built with Python. The application allows users to perform basic CRUD operations (Create, Read, Update, Delete) on car records. It uses object-oriented programming and stores data in-memory using dictionaries, so no database is required.

---

## 📁 Project Contents

- `application.py` – Main menu-driven interface for user interaction  
- `models.py` – Defines the `Car` data class with attributes like ID, brand, model, year, price, and color  
- `operations.py` – Handles all business logic (add, update, delete, retrieve cars)

---

## 🧩 Project Modules & Responsibilities

### 1. `models.py`
- Defines the `Car` class that represents a car with attributes:  
  `car_id`, `brand`, `model`, `year`, `price`, `color`
- Includes:
  - `__str__` method to display car details
  - `update_info` method to modify car attributes

### 2. `operations.py`
- Stores car data in a dictionary using `car_id` as the key
- Provides functions for CRUD operations:
  - **Add a car**
  - **Update a car**
  - **Delete a car**
  - **Get car by ID**
  - **Show all cars**

### 3. `application.py`
- Runs the interactive CLI menu
- Takes input using `input()`
- Calls functions from `operations.py` based on user choice

---
## 🧩 Features

- **Add Cars** – Input and store new car details
- **Update Cars** – Modify existing car information
- **View All Cars** – Display all cars in the system
- **Delete Cars** – Remove a car using its ID
- **Search by ID** – View details of a specific car

 
 

 
