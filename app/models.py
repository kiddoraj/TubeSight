from app import db

class Video(db.Model):
    video_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    

    class Channel(db.Model):
        channel_id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255), nullable=False)
        description = db.Column(db.String(255), nullable=False)
        videos = db.relationship('Video', backref='channel', lazy=True)
        url = db.Column(db.String(255), nullable=False)
        channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)


        class user(db.Model):
            user_id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(255), nullable=False)
            email = db.Column(db.String(255), nullable=False)
            password = db.Column(db.String(255), nullable=False)
            saved_videos = db.relationship('Video', secondary = 'user_saved_videos', backref='user', lazy=True)
            liked_videos = db.relationship('Video', secondary = 'user_liked_videos', backref='user')
            subscribed_channels = db.relationship("Channel", secondary = 'User_subscribed_channels', backref = 'users')
           


        #class Like(db.Model):
        #   id = db.Column(db.Integer, primary_key=True)
        #  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        # comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)
            #created_at = db.Column(db.DateTime, nullable=False)
            #updated_at = db.Column(db.DateTime, nullable=False)
            #deleted_at = db.Column(db.DateTime, nullable=True)
            #__table_args__ = (db.UniqueConstraint('user_id', 'comment_id', name='_user_comment_uc'),)


    # Define the relationship between the User and Video models
    #
        user_saved_videos = db.Table ('user_saved_videos',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
        db.Column('video_id', db.Integer, db.ForeignKey('video.id'), primary_key=True)
        )

        user_liked_videos = db.Table('user_liked_videos',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
        db.Column('video_id', db.Integer, db.ForeignKey('video.id'), primary_key=True)
        )

        user_subscribed_channels = db.Table('user_subscribed_channels',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
        db.Column('channel_id', db.Integer, db.ForeignKey('channel.id'), primary_key=True)
        )