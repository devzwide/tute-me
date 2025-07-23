from app.extensions import db

class Module(db.Model):
    __tablename__ = 'modules'
    module_id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(80), nullable=False)
    module_code = db.Column(db.String(10), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)

