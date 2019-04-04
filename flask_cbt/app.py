from flask import *
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

app = Flask(__name__)
# Created a table in the database
# import mysql.connector
# #
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='paulawolesi',
#     passwd='@Shiningstar01',
#     database='myflaslapp'
# )
#
# mycursor = mydb.cursor()
# mycursor.execute(
#     'CREATE TABLE cbt_users(id INT(11) AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100), email VARCHAR(100), username VARCHAR(30), password VARCHAR(200), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP) ')

#config MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'paulawolesi'
app.config['MYSQL_PASSWORD'] = '@Shiningstar01'
app.config['MYSQL_DB'] = 'myflaslapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

@app.route('/index')
def index():
    return render_template('index.html')
#login
@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form fields
        username = request.form['username']
        password_candidate = request.form['password']

        # create cursor
        cur = mysql.connection.cursor()

        #Get user by username
        result = cur.execute('SELECT * FROM cbt_users WHERE username = %s', [username])

        if result > 0:
            #Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare PAsswords
            if sha256_crypt.verify(password_candidate, password):
               #passed
               session['logged_in'] = True
               session['username'] = username

               flash('You are now logged in','success')
               return redirect(url_for('dashboard'))

            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()

        else:
            error = 'Username not found'
            return render_template('login.html',error=error)
    return render_template('login.html')


# Register form class
class registerForm(Form):
    name = StringField('Name',[validators.Length(min=1, max=50)])
    username = StringField('Username',[validators.Length(min=4, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.data_required(),
        validators.EqualTo('confirm', message= 'Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


# USer register
@app.route('/register', methods=['GET','POST'])
def register():
    form = registerForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #Create cursor
        cur = mysql.connection.cursor()

        #Execute query
        cur.execute("INSERT INTO cbt_users(name, email, username, password) VALUE(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)


#logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out','success')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)