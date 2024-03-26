from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegistrationForm, SearchForm, BookmarkForm, NotificationForm, CommentForm, LikeForm, ForumThreadForm, ForumPostForm, UploadForm
from config import config

app = Flask(__name__)
app.config.from_object(config[os.getenv('venv') or 'default'])
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Your models go here

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/bookmark', methods=['POST'])
@login_required
def bookmark():
    form = BookmarkForm()
    if form.validate_on_submit():
        # Add bookmark logic here
        pass
    return redirect(url_for('home'))

@app.route('/notification', methods=['POST'])
@login_required
def notification():
    form = NotificationForm()
    if form.validate_on_submit():
        # Add notification logic here
        pass
    return redirect(url_for('home'))

@app.route('/comment', methods=['POST'])
@login_required
def comment():
    form = CommentForm()
    if form.validate_on_submit():
        # Add comment logic here
        pass
    return redirect(url_for('home'))

@app.route('/like', methods=['POST'])
@login_required
def like():
    form = LikeForm()
    if form.validate_on_submit():
        # Add like logic here
        pass
    return redirect(url_for('home'))

@app.route('/forum', methods=['POST'])
@login_required
def forum():
    form = ForumThreadForm()
    if form.validate_on_submit():
        # Add forum thread logic here
        pass
    return redirect(url_for('home'))

@app.route('/post', methods=['POST'])
@login_required
def post():
    form = ForumPostForm()
    if form.validate_on_submit():
        # Add forum post logic here
        pass
    return redirect(url_for('home'))

@app.route('/upload', methods=['POST'])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        # Add file upload logic here
        pass
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)