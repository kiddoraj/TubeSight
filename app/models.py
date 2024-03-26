from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    bookmarks = db.relationship('Bookmark', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    likes = db.relationship('Like', backref='user', lazy=True)
    channels = db.relationship('Channel', backref='creator', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    url = db.Column(db.String(200), nullable=False, unique=True)
    duration = db.Column(db.Integer, nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)
    likes = db.Column(db.Integer, default=0)
    comments = db.relationship('Comment', backref='video', lazy=True)
    bookmarks = db.relationship('Bookmark', backref='video', lazy=True)
    notifications = db.relationship('Notification', backref='video', lazy=True)
    likes = db.relationship('Like', backref='video', lazy=True)

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subscribers = db.Column(db.Integer, default=0)
    bookmarks = db.relationship('Bookmark', backref='channel', lazy=True)
    notifications = db.relationship('Notification', backref='channel', lazy=True)

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=True)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=True)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=True)
    notification_type = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
