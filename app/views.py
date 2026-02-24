from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


def format_date_joined(date):
    return date.strftime("%B, %Y")


@app.route('/profile')
def profile():
    """
    Fake profile page (static placeholder data)
    """
    full_name = "Daniel England"
    username = "@dengland"
    location = "Kingston, Jamaica"
    bio = "football, swimming and building cool apps."

    posts = 10
    followers = 1500
    following = 600

    # specific date you "joined"
    date_joined = datetime.date(2026, 2, 10)
    joined = format_date_joined(date_joined)

    return render_template(
        "profile.html",
        full_name=full_name,
        username=username,
        location=location,
        date_joined=joined,
        bio=bio,
        posts=posts,
        followers=followers,
        following=following
    )

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
  
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404