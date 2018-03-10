from src import db


class CPU(db.Model):
    __tablename__ = "computer_devices"
    id = db.Column(db.String(80), primary_key=True)
    model_no = db.Column(db.String(80))
    name = db.Column(db.String(80), unique=True)
    service_tag = db.Column(db.String(80), unique=True)
    os_type = db.Column(db.Integer)
    keyboard_id = db.Column(db.String(80), unique=True)
    monitor_id = db.Column(db.String(80), unique=True)
    mouse_id = db.Column(db.String(80), unique=True)
    product_key = db.Column(db.String(80), unique=True, nullable=True)  # some computers don't have a product key listed
    uwi_tag = db.Column(db.String(80), unique=True, nullable=True)  # some computers don't have a tag
    status = db.Column(db.String(80))

    def __init__(self, model_no, name, service_tag, os_type, keyboard_id, monitor_id, mouse_id,
                 product_key, uwi_tag):
        self.id = str(model_no) + str(service_tag)
        self.model_no = model_no
        self.name = name
        self.service_tag = service_tag
        self.os_type = os_type
        self.keyboard_id = keyboard_id
        self.monitor_id = monitor_id
        self.mouse_id = mouse_id
        self.product_key = product_key
        self.uwi_tag = uwi_tag
        self.status = 'ONLINE'

    def change_status(self):
        if self.status == 'ONLINE':
            self.status = 'OFFLINE'
        else:
            self.status = 'ONLINE'

