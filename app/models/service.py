# from app.models import db
#
#
# class Service(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60), unique=True, nullable=False)
#     description = db.Column(db.String(150), unique=True, nullable=False)
#     url = db.Column(db.String(60), nullable=False)
#     user_id = db.relationship('Password', backref='owner', lazy=True)
