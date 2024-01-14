from flask import Flask, jsonify, request
from api_utils import get_random_users, get_user_with_favorite_drink

app = Flask(__name__)

@app.route('/users', methods=['Get'])
def get_users():
    limit = int(request.args.get('limit', 10))
    categorize = request.args.get('categorize')
    
    data = get_random_users(limit, categorize)
    return jsonify(data)

