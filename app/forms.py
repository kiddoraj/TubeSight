from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, HiddenField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')

class BookmarkForm(FlaskForm):
    id = HiddenField('ID', validators=[DataRequired()])
    submit = SubmitField('Bookmark')

class NotificationForm(FlaskForm):
    new_videos = BooleanField('New Videos')
    recommendations = BooleanField('Recommendations')
    submit = SubmitField('Update Preferences')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')

class LikeForm(FlaskForm):
    id = HiddenField('ID', validators=[DataRequired()])
    submit = SubmitField('Like')

class ForumThreadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post = TextAreaField('Post', validators=[DataRequired()])
    submit = SubmitField('Create Thread')

class ForumPostForm(FlaskForm):
    post = TextAreaField('Post', validators=[DataRequired()])
    submit = SubmitField('Post Reply')

class UploadForm(FlaskForm):
    file = FileField('File', validators=[DataRequired()])
    submit = SubmitField('Upload')