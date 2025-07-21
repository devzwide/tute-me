import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    DB_PATH = os.environ.get('DB_PATH', os.path.join(BASE_DIR, 'instance', 'peer_tutoring.db'))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    print(f"Configuration loaded: {BASE_DIR}, DB Path: {DB_PATH}")