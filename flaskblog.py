from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = "secretkey"


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title = 'home',)


@app.route("/about")
def about():
    return render_template('about.html',title = 'about')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',form = form)


# Custom Error Pages :
# Invalid URL:

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html",e = 404)


@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html", e = 500)


@app.route('/dummyposts')
def dummy_post():
    return render_template("dummypost.html",posts = posts)


@app.route("/ContactUs")
def contact_page():
    return render_template('contact_page.html')


if __name__ == '__main__':
    app.run(debug=True)

