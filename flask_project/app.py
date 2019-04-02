from flask import *
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.debug = True

#config MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'paulawolesi'
app.config['MYSQL_PASSWORD'] = '@Shiningstar01'
app.config['MYSQL_DB'] = 'myflaslapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

Articles = Articles()

#Index
@app.route('/')
def index():
    return render_template('home.html')

#About
@app.route('/about')
def about():
    return render_template('about.html')

# Articles
@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

# Single article
@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id = id)

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
        cur.execute("INSERT INTO users(name, email, username, password) VALUE(%s, %s, %s, %s)", (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('index'))
    return render_template('register.html', form=form)
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
        result = cur.execute('SELECT * FROM users WHERE username = %s', [username])

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

#logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out','success')
    return redirect(url_for('login'))

#Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == ("__main__"):
    app.secret_key = 'secret123'
    app.run()