from flask import *
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)