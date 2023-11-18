import os
from flask import Flask

from app.models.models import db
from app.routes.routes import book_bp

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = 'sqlite:///'+os.path.join(base_dir, 'database/book.db')
app.config['SQLALCHEMY_DATABASE_URI'] = db_path

db.init_app(app)
app.register_blueprint(book_bp)

if __name__ == '__main__':
    app.run(debug=True)
