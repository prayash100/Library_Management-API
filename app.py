from flask import Flask, request, jsonify
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Mastery", "author": "Robert Greene", "year": 2012},
    {"id": 2, "title": "Rich Dad Poor Dad", "author": "Robert T. Kiyosaki", "year": 1997}
]

members = [
    {"id": 1, "name": "Chandan", "email": "chandan@gmail.com"},
    {"id": 2, "name": "Prayash", "email": "vinayakppj123@gmail.com"}
]

# Sample token (in a real project, tokens would be dynamically generated)
VALID_TOKEN = "aaaaaa12"

# Function to check if the request has a valid token
def check_authentication():
    token = request.headers.get('Authorization')
    if token != VALID_TOKEN:
        return jsonify({"message": "Unauthorized"}), 401
    return None

# 1. Create a new book (POST /books)
@app.route('/books/', methods=['POST'])
def add_book():
    error = check_authentication()
    if error:
        return error
    
    # Get data from the request
    data = request.get_json()
    if not data or not data.get("title") or not data.get("author"):
        raise BadRequest("Title and Author are required")

    # Create a new book
    new_id = len(books) + 1
    new_book = {
        "id": new_id,
        "title": data["title"],
        "author": data["author"],
        "year": data.get("year", 2023)  # Default to current year if no year is provided
    }
    books.append(new_book)
    return jsonify(new_book), 201

# 2. Get all books with optional search and pagination (GET /books)
@app.route('/books/', methods=['GET'])
def get_books():
    error = check_authentication()
    if error:
        return error

    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    # Filter by title or author if provided
    filtered_books = books
    if title:
        filtered_books = [book for book in books if title.lower() in book['title'].lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book['author'].lower()]

    # Implement pagination
    start = (page - 1) * per_page
    end = start + per_page
    paginated_books = filtered_books[start:end]

    return jsonify(paginated_books)

# 3. Update a book by ID (PUT /books/{id})
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    error = check_authentication()
    if error:
        return error

    # Find the book by ID
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        raise NotFound("Book not found")

    # Get updated data from the request
    data = request.get_json()
    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    book['year'] = data.get('year', book['year'])

    return jsonify(book)

# 4. Delete a book by ID (DELETE /books/{id})
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    error = check_authentication()
    if error:
        return error

    # Find the book by ID
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        raise NotFound("Book not found")

    # Delete the book
    books.remove(book)
    return jsonify({"message": "Book deleted successfully"})

# 5. Create a new member (POST /members)
@app.route('/members/', methods=['POST'])
def add_member():
    error = check_authentication()
    if error:
        return error
    
    # Get data from the request
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        raise BadRequest("Name and Email are required")

    # Create a new member
    new_id = len(members) + 1
    new_member = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"]
    }
    members.append(new_member)
    return jsonify(new_member), 201

# 6. Get all members (GET /members)
@app.route('/members/', methods=['GET'])
def get_members():
    error = check_authentication()
    if error:
        return error
    return jsonify(members)

# 7. Update a member by ID (PUT /members/{id})
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    error = check_authentication()
    if error:
        return error

    # Find the member by ID
    member = next((m for m in members if m['id'] == id), None)
    if not member:
        raise NotFound("Member not found")

    # Get updated data from the request
    data = request.get_json()
    member['name'] = data.get('name', member['name'])
    member['email'] = data.get('email', member['email'])

    return jsonify(member)

# 8. Delete a member by ID (DELETE /members/{id})
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    error = check_authentication()
    if error:
        return error

    # Find the member by ID
    member = next((m for m in members if m['id'] == id), None)
    if not member:
        raise NotFound("Member not found")

    # Delete the member
    members.remove(member)
    return jsonify({"message": "Member deleted successfully"})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
