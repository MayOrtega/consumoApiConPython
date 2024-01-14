from flask import Flask, jsonify, request
from api_utils import get_random_users, get_user_with_favorite_drink

app = Flask(__name__)

@app.route('/users', methods=['Get'])
def get_users():
    limit = int(request.args.get('limit', 10))
    categorize = request.args.get('categorize')
    
    data = get_random_users(limit, categorize)
    return jsonify(data)

@app.route('/users', methods=['Get'])
def get_users_with_favorite_drink():
    data = get_user_with_favorite_drink
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

