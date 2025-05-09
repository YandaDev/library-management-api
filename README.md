# Library Management System API

## Description

The **Library Management System API** is a complete database management system designed to manage a small library. It allows users to perform CRUD (Create, Read, Update, Delete) operations on library members, books, and borrowed records. The project combines a well-structured relational database in MySQL with a FastAPI backend to provide a seamless and efficient API for managing library operations.

This project was developed as part of an exercise to design and implement a full-featured database and integrate it with a programming language to create a working CRUD API.


## Features

- **Database Design**:
  - A relational database built using MySQL.
  - Includes tables for `members`, `books`, and `borrowed_books` with proper constraints (Primary Keys, Foreign Keys, NOT NULL, UNIQUE).
  - Relationships include:
    - One-to-Many: Members borrowing multiple books.
    - Many-to-Many: Books borrowed by multiple members.

- **API Functionality**:
  - Built using FastAPI for a lightweight and high-performance backend.
  - Endpoints to manage:
    - Members: Add and list library members.
    - Books: Add and manage books in the library.
    - Borrowed Records: Track which books are borrowed and by whom.

- **CRUD Operations**:
  - Create, Read, Update, and Delete operations implemented for all entities.


## Technologies Used

- **MySQL**: For the relational database.
- **FastAPI**: For the backend API.
- **Python**: For implementing the API logic.
- **VSCode**: For development.
- **GitHub**: For version control.



## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YandaDev/library-management-api.git
   cd library-management-api
   ```

2. **Create & Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Set your MySQL credentials in the `.env` file:
   ```properties
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=root
   DB_NAME=library_db
   DB_PASSWORD=your_password
   ```

5. **Import the Database**:
   - Open MySQL Workbench or your preferred MySQL client.
   - Run the `schema.sql` file to create the database and tables.

6. **Run the FastAPI Server**:
   ```bash
   uvicorn api.main:app --reload
   ```



## API Endpoints

### Members
- **GET /members**: List all members.
- **POST /members**: Add a new member.

### Books (Future Implementation)
- **GET /books**: List all books.
- **POST /books**: Add a new book.

### Borrowed Records (Future Implementation)
- **GET /borrowed**: List all borrowed books.
- **POST /borrowed**: Add a new borrowed record.


## Entity-Relationship Diagram (ERD)

![Entity-Relationship Diagram (ERD)](docs/erd.png)



## Deliverables

- **Database Schema**: The `schema.sql` file contains all `CREATE TABLE` statements and sample data.
- **API Code**: The FastAPI implementation connects to the MySQL database and provides CRUD functionality.

