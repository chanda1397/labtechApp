from src import db
from src.models import LabTech
from src.models import CPU
from src.models import Maintenance


class DatabaseModel:
    def __init__(self):
        self.db = db

    def create_new_user(self, student_id, first_name, last_name, email, password, status, account_type="ASSISTANT"):
        """
        :param account_type:
        :param status:
        :param password:
        :param email:
        :param last_name:
        :param first_name:
        :type student_id: int
        """
        # type: (int, str, str, str, str, str, str, str) -> None
        self.db.session.add(LabTech(student_id, first_name, last_name, email, password, status, account_type))
        self.db.session.commit()

    def commit(self):
        self.db.session.commit()

    def create_cpu(self, name, model_no, service_tag, os_type, keyboard_id, monitor_id, mouse_id,
                   product_key=None, uwi_tag=None):
        self.db.session.add(CPU(name, model_no, service_tag, os_type, keyboard_id, monitor_id, mouse_id,
                                product_key, uwi_tag))
        self.db.session.commit()

    def device_maintenance(self, device_id, attendee_id):
        device = Maintenance.query.filter_by(device_id=device_id).first()
        if not device:
            self.db.session.add(Maintenance(device_id, attendee_id))
        else:
            device.update_maintained(attendee_id)
        self.db.session.commit()

    @staticmethod
    def find_cpu_by_name(name):
        return CPU.query.filter_by(name=name).first()

    @staticmethod
    def find_user_by_id(_id):
        # type: (int) -> LabTech
        return LabTech.query.filter_by(id=_id).first()
