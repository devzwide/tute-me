from app.extensions import db

class Booking(db.Model):
    __tablename__ = 'bookings'
    booking_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    booking_date = db.Column(db.Date, nullable=False)
