from flask import Flask, render_template, request, \
      session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register2.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
