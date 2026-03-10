import jwt
import bcrypt
from functools import wraps
from flask import request, jsonify

SECRET_KEY = 'your_secret_key'

# Password hashing function
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Function to verify password

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Token generation function

def generate_token(user_id, role):
    token = jwt.encode({'user_id': user_id, 'role': role}, SECRET_KEY, algorithm='HS256')
    return token

# Decorator for role-based access control

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing!'}), 403
            try:
                data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            except Exception:
                return jsonify({'message': 'Token is invalid!'}), 403
            if data['role'] != role:
                return jsonify({'message': 'Unauthorized!'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Example of using hash_password and verify_password
if __name__ == '__main__':
    hashed = hash_password('my_password')
    print('Hashed password:', hashed)
    print('Password verification:', verify_password('my_password', hashed))
