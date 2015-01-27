from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    
    posts = [
            {'author': {'nickname': 'John'},
             'body' : 'Such a day'
                }
    ]

    user = {'nickname': 'Kacper'} #mockup
    return render_template('index.html',
                           title='Home',
                           user = user,
                           posts=posts)
