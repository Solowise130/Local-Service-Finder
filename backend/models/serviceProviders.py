from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ServiceProvider(db.Model):
    __tablename__ = 'service_providers'

    provider_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    
    
    user = db.relationship('User', backref=db.backref('service_providers', lazy=True))

    def __init__(self, user_id, company_name, description=None, location=None):
        self.user_id = user_id
        self.company_name = company_name
        self.description = description
        self.location = location