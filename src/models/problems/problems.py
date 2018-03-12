from src import db


class Problems(db.Model):
    # whenever a device has a problem, the database will log the problem(s) along with the device (monitor, mouse,
    # keyboard, port etc).
    __tablename__ = "device_problems"
    id = db.Column(db.String(80), primary_key=True)
    device_id = db.Column(db.String(80), unique=True)
    problem = db.Column(db.String(255), unique=True)
    logged_by = db.Column(db.String(80))
    attendee = db.Column(db.String(80))

    def __init__(self, device_id, problem):
        self.device_id = device_id
        self.problem = problem
