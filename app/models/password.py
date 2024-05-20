from cryptography.fernet import Fernet

from app.models import db


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    service_url = db.Column(db.String(255), nullable=False)
    service_username = db.Column(db.String(150), nullable=True)
    service_email = db.Column(db.String(150), nullable=True)
    service_phone = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def encrypt_password(self, password, key):
        f = Fernet(key)
        self.password = f.encrypt(password.encode()).decode()

    def decrypt_password(self, key):
        f = Fernet(key)
        return f.decrypt(self.password.encode()).decode()
