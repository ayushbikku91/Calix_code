from flask import Flask, request, jsonify

app = Flask(__name__)

# Create a list of users.
users = []

# Create a GET endpoint to get all users.
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify(users)

# Create a POST endpoint to create a new user.
@app.route("/users", methods=["POST"])
def create_user():
    user = request.json
    users.append(user)
    return jsonify(user)

# Create a GET endpoint to get a single user by ID.
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = users[user_id]
    return jsonify(user)

# Create a PUT endpoint to update a user.
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = request.json
    users[user_id] = user
    return jsonify(user)

# Create a DELETE endpoint to delete a user.
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    users.pop(user_id)
    return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)
