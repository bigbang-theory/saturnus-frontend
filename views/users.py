from flask import Flask, render_template, request
from saturnus-backend/users/models.users import User

app = Flask(__name__)

"""Register process"""    
@app.route('/register', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # insert data to database
        model = User()
        data = model(first_name, last_name, username, email, password)
    return render_template('/templates/users/login.html')

if __name__ == '__main__':
    app.run(debug=True)