from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_complexity(password):
    min_length = 8
    if len(password) < min_length:
        return "Password must be at least 8 characters long."
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."
    if not re.search(r'[\W_]', password):  # \W matches any non-word character
        return "Password must contain at least one special character."
    return "Password is strong."

@app.route('/')
def index():
    return render_template('password_checker.html')

@app.route('/check', methods=['POST'])
def check():
    password = request.form['password']
    result = check_password_complexity(password)
    return render_template('password_checker.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
