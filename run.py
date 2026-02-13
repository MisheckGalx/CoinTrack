from flask import Flask
from app import create_app
from app.models import db

app = Flask(__name__, static_folder='app/static', static_url_path='/static')

with app.app_context():
	# create all database tables
	db.create_all()


if __name__ == "__main__":
	app.run(debug=True)
