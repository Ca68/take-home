from app import create_app, db
from app.models import User

app = create_app()

def make_context():
    return {
        'db': db,
        'User': User

    }