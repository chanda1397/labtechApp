from src.models.cpu.cpu import CPU
from src.models.leb_tech.lab_tech import LabTech


class Database(object):
    def __init__(self, db):
        self.db = db

    def create_new_user(self, first_name, last_name, email, password, student_id, status, account_type = 0):
        self.db.session.add(LabTech(first_name, last_name, email, password, student_id, status, account_type))
        self.db.session.commit()

    @staticmethod
    def find_user_by_id(_id):
        user = LabTech.query.filter_by(id = _id).first()
        if user:
            return user
        return None

    def create_cpu(self, name, model_no, service_tag, os_type, keyboard_id, monitor_id, mouse_id,
                   product_key = None, uwi_tag = None):

        self.db.session.add(CPU(name, model_no, service_tag, os_type, keyboard_id, monitor_id, mouse_id,
                                product_key, uwi_tag))
        self.db.session.commit()
