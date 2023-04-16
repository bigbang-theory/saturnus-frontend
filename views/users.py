from flask import Flask, render_template, Blueprint
import request

# app = Flask(__name__)
users_view = Blueprint('users_view', __name__, url_prefix='/users')

"""Register process"""    
@users_view.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        payload = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
        }
        
        send_request = request.post('http://localhost:8000/users', json=payload).json()

        # check response from the server
        if send_request.get('status') == 'success':
            return render_template('login.html',)
        else:
            # error_message = send_request.get('Your registration is not successful')
            return render_template('signup.html',)

    return render_template('signup.html')