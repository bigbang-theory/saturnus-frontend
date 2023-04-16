from flask import Flask
from views.users import users_view

app = Flask(__name__)

app.register_blueprint(users_view)

if __name__ == '__main__':
    app.run(debug=True, port=8002)