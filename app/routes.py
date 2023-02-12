from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'blunt'}
    posts = [
        {
            'author':{'username':'Robert Duvall'},
            'body': 'Love the smell of napalm in the morning!'
        },
        {
            'author':{'username':'Ruth Wilson'},
            'body': 'You can\'t prove a negative. It just cannot be done!'
        }
    ]

    return render_template('index.html', title = 'Home', user = user, posts = posts)


