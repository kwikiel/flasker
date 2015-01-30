from flask import Flask
from flask.ext.sqlalechemy import SQLAlechemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from app import views,models
