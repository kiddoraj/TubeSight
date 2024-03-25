from flask import render_template, request
from app import app, db
from app.models import Video

@app.route('/')
def index():
    # Add code to retrieve and display the homepage
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    videos = Video.query.filter(Video.title.ilike(f'%{query}%')).all()
    return render_template('search.html', videos=videos)

@app.route('/video/<int:video_id>')
def video_details(video_id):
    video = Video.query.get_or_404(video_id)
    # Add code to display the details of the video
    return render_template('video.html', video=video)

@app.route('/channel/<int:channel_id>')
def channel_details(channel_id):
    # Add code to retrieve and display the details of the channel
    return render_template('channel.html')

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    # Add code to retrieve and display the user profile
    return render_template('user.html')