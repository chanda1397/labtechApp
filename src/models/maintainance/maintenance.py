from datetime import datetime
from src import db


class Maintenance(db.Model):
    __tablename__ = "maintenance"
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(80), unique=True)
    attendee_id = db.Column(db.String(80))
    maintained = db.Column(db.String(80))

    def __init__(self, device_id, attendee_id):
        self.device_id = device_id
        self.attendee_id = attendee_id
        self.maintained = datetime.now().isoformat(" ")

    def update_maintained(self, attendee_id):
        self.attendee_id = attendee_id
        self.maintained = datetime.now().isoformat(" ")