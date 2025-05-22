# 🚀 Simple Flask CRUD API

---

## Table of Contents
* [About](#-about)
* [Features](#-features)
* [Getting Started](#-getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Running the API](#running-the-api)
    * [Database Setup](#database-setup)
* [API Endpoints](#-api-endpoints)
    * [Drinks Resource](#drinks-resource)

---

## 💡 About

This is a straightforward RESTful API built with **Flask** and **Flask-SQLAlchemy**, demonstrating essential **CRUD** (Create, Read, Update, Delete) operations on a "Drinks" resource. It's a great starting point for understanding how to build basic APIs with Python's micro-framework.

---

## ✨ Features

* **Create Drinks:** Add new drink entries to your database.
* **Read Drinks:** Fetch a list of all drinks or a specific drink by its ID.
* **Update Drinks:** Modify details of existing drinks.
* **Delete Drinks:** Remove drink entries from the database.
* Uses **SQLite** for simple, file-based database storage.
* Handles requests and responses using **JSON** format.

---

## 🚀 Getting Started

Follow these steps to get the API up and running on your local machine.

### Prerequisites

Make sure you have these installed:

* **Python 3.8+**
* **pip** (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd [your_project_name] # e.g., cd flask-drink-api
    ```

2.  **Create and activate a virtual environment:**
    Using a virtual environment is crucial for managing project dependencies without conflicts.

    ```bash
    python3 -m venv .venv
    source .venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On MacOS
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    *(If you haven't created `requirements.txt` yet, install Flask and Flask-SQLAlchemy, then run `pip freeze > requirements.txt`)*

### Running the API

1.  **Set the Flask application environment variable:**
    This tells Flask where your main application file is located.

    ```bash
    export FLASK_APP=app.py # On Windows CMD: set FLASK_APP=app.py
    export FLASK_ENV=development # Optional: Enables Flask's debugger and reloader
    ```
    
2.  **Start the Flask development server:**

    ```bash
    flask run
    ```
    The API will typically be accessible at `http://127.0.0.1:5000/`.

### Database Setup

You need to create the database tables before the API can store any data.

1.  **Create the `create_db.py` script:**
    This dedicated script ensures your database tables are set up correctly within the Flask application context.

    ```python
    # create_db.py
    from app import app, db # Ensure this import path is correct for your project

    if __name__ == '__main__':
        with app.app_context(): # This pushes the necessary application context
            db.create_all()
            print("Database tables created successfully!")
    ```

2.  **Run the database creation script:**

    ```bash
    python create_db.py
    ```
    This will create a `data.db` file in your project's root directory.

---

## ⚡ API Endpoints

The API provides routes for managing `drinks`. All requests and responses use **JSON** format.

### Drinks Resource

| Method   | Endpoint          | Description                          | Request Body Example                                       | Success Response Example                                                                           | Error Response Example                                  |
| :------- | :---------------- | :----------------------------------- | :--------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| `POST`   | `/drinks`         | Create a new drink                   | `{"name": "Espresso", "description": "Strong coffee"}`     | `201 Created`, `{"message": "Drink created successfully!", "drink": {"id": 1, "name": "Espresso", "description": "Strong coffee"}}` | `400 Bad Request`, `{"message": "Name is required"}`    |
| `GET`    | `/drinks`         | Retrieve all drinks                  | (None)                                                     | `200 OK`, `{"drinks": [{"id": 1, "name": "Espresso", ...}, {"id": 2, "name": "Latte", ...}]}`      | (None)                                                  |
| `GET`    | `/drinks/<id>`    | Retrieve a single drink by ID        | (None)                                                     | `200 OK`, `{"id": 1, "name": "Espresso", "description": "Strong coffee"}`                        | `404 Not Found`, `{"message": "Drink not found"}`       |
| `PUT`    | `/drinks/<id>`    | Update an existing drink by ID       | `{"name": "Espresso", "description": "Very strong coffee"}`| `200 OK`, `{"message": "Drink updated successfully!", "drink": {"id": 1, "name": "Espresso", "description": "Very strong coffee"}}` | `404 Not Found`, `{"message": "Drink not found"}`       |
| `DELETE` | `/drinks/<id>`    | Delete a drink by ID                 | (None)                                                     | `204 No Content` (empty response body)                                                             | `404 Not Found`, `{"message": "Drink not found"}`       |
