
# Library Management API

This project provides a **Library Management API** that allows you to manage books and members in a library system. It supports basic CRUD operations (Create, Read, Update, Delete) for managing books and members. The API is deployed and accessible at the following URL:

[https://library-management-api-4ykh.onrender.com](https://library-management-api-4ykh.onrender.com)

**Authorization Header**: All API requests require an **Authorization** key in the header. During the demonstration, you can use the following static authorization key for authentication:

- **Authorization Key**: `aaaaaa12`

For future implementations in a real-life scenario, this key would be dynamic and could be tied to user roles or other secure methods of authentication.

---

## API Endpoints

The following sections describe the API endpoints available to interact with the system. Ensure you include the **Authorization** key in the header for each request.

---

### **Books Endpoints**

#### 1. **Get All Books** - `GET /books/`

This endpoint allows you to retrieve a list of all books in the library.

- **Method:** GET
- **URL:** `https://library-management-api-4ykh.onrender.com/books/`
- **Header (Authorization)**: `Authorization: aaaaaa12`

##### Example Response:
```json
[
  {
    "id": 1,
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "year": 1951
  },
  {
    "id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960
  }
]
```

---

#### 2. **Add a New Book** - `POST /books/`

This endpoint allows you to add a new book to the library.

- **Method:** POST
- **URL:** `https://library-management-api-4ykh.onrender.com/books/`
- **Request Body:**
  ```json
  {
    "title": "Book Title",
    "author": "Author Name",
    "year": 2023
  }
  ```
- **Header (Authorization)**: `Authorization: aaaaaa12`

##### Example Response:
```json
{
  "id": 3,
  "title": "New Book",
  "author": "Author Name",
  "year": 2023
}
```

---

#### 3. **Update a Book** - `PUT /books/{id}`

This endpoint allows you to update the details of an existing book in the library.

- **Method:** PUT
- **URL:** `https://library-management-api-4ykh.onrender.com/books/{id}`
  - Replace `{id}` with the ID of the book you want to update.
- **Request Body:**
  ```json
  {
    "title": "Updated Book Title",
    "author": "Updated Author",
    "year": 2024
  }
  ```
- **Header (Authorization)**: `Authorization: aaaaaa12`

##### Example Response:
```json
{
  "id": 1,
  "title": "Updated Book Title",
  "author": "Updated Author",
  "year": 2024
}
```

---

#### 4. **Delete a Book** - `DELETE /books/{id}`

This endpoint allows you to delete a book from the library.

- **Method:** DELETE
- **URL:** `https://library-management-api-4ykh.onrender.com/books/{id}`
  - Replace `{id}` with the ID of the book you want to delete.
- **Header (Authorization)**: `Authorization: aaaaaa12`

##### Example Response:
```json
{
  "message": "Book with id 1 has been deleted."
}
```

---

### **Members Endpoints**

#### 1. **Get All Members** - `GET /members/`

This endpoint allows you to retrieve a list of all members of the library.

- **Method:** GET
- **URL:** `https://library-management-api-4ykh.onrender.com/members/`
- **Header (Authorization)**: `Authorization: aaaaaa12`

##### Example Response:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "janesmith@example.com"
  }
]
```

---

#### 2. **Add a New Member** - `POST /members/`

This endpoint allows you to add a new member to the library system.

- **Method:** POST
- **URL:** `https://library-management-api-4ykh.onrender.com/members/`
- **Request Body:**
  ```json
  {
    "name": "New Member",
    "email": "newmember@example.com"
  }
  ```
- **Header (Authorization)**: `Authorization: aaaaaa12`

##### Example Response:
```json
{
  "id": 3,
  "name": "New Member",
  "email": "newmember@example.com"
}
```

---

#### 3. **Update a Member** - `PUT /members/{id}`

This endpoint allows you to update an existing member's details.

- **Method:** PUT
- **URL:** `https://library-management-api-4ykh.onrender.com/members/{id}`
  - Replace `{id}` with the ID of the member you want to update.
- **Request Body:**
  ```json
  {
    "name": "Updated Name",
    "email": "updatedemail@example.com"
  }
  ```
- **Header (Authorization)**: `Authorization: aaaaaa12`

##### Example Response:
```json
{
  "id": 1,
  "name": "Updated Name",
  "email": "updatedemail@example.com"
}
```

---

#### 4. **Delete a Member** - `DELETE /members/{id}`

This endpoint allows you to delete a member from the library.

- **Method:** DELETE
- **URL:** `https://library-management-api-4ykh.onrender.com/members/{id}`
  - Replace `{id}` with the ID of the member you want to delete.
- **Header (Authorization)**: `Authorization: aaaaaa12`

##### Example Response:
```json
{
  "message": "Member with id 1 has been deleted."
}
```

---

## How to Use the API with Postman

To interact with the API using **Postman**, follow these steps:

1. Open **Postman** and create a new request.
2. Set the **method** (GET, POST, PUT, DELETE) based on the operation you want to perform.
3. Enter the API URL, for example:  
   `https://library-management-api-4ykh.onrender.com/books/` (for the GET request).
4. In the **Headers** section, add the **Authorization** key with the value `aaaaaa12`:
   - Key: `Authorization`
   - Value: `aaaaaa12`
5. If you're making a **POST** or **PUT** request, add the necessary JSON data in the **Body** section of Postman.
6. Click **Send** to make the request and see the response.

---

## How to Run the Project Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/{your-username}/Library_Management_API.git
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.7+ installed. Then, install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API**:
   After installing the dependencies, you can run the Flask application locally:
   ```bash
   python app.py
   ```

   This will start the server, and the API will be available at `http://127.0.0.1:5000`.

4. **Test the Endpoints**:
   You can now test the API using tools like Postman or curl with the same endpoints listed above.

---

## Design Choices

- **Flask Framework**: I chose Flask because it's lightweight, easy to set up, and highly suitable for building RESTful APIs quickly.
- **In-Memory Data Storage**: For simplicity and demonstration purposes, this API uses in-memory storage to manage books and members (stored in Python lists). This means the data will be lost once the server stops. For production use, a database like SQLite or PostgreSQL should be used.

---

## Assumptions and Limitations

- **Authentication**: This API uses a static **Authorization** key for authentication. In a real-life scenario, this key would be dynamic and tied to user roles or other secure methods of authentication.
- **In-Memory Storage**: The API does not persist data once the server restarts because it uses in-memory lists. A database solution is recommended for production use.
- **Error Handling**: Basic error handling is implemented (e.g., 404 Not Found for missing resources). However, more detailed error responses and validation could be added for better user experience.

---

## Conclusion

This API provides a simple way to manage a library's books and members. It allows users to add, update, delete, and view books and members in the system. The deployment is live at [https://library-management-api-4ykh.onrender.com](https://library-management-api-4ykh.onrender.com), and you can interact with it using Postman or curl.
