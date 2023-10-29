from models import db, Flag, Environment
from events.signals import new_flag_signal, flag_status_signal

class FlagManager:

    def create(self, flag: Flag, environments: list[str]):
        if environments:
            envs = list(map(lambda env: Environment.query.get(env), environments))
            for e in envs: flag.environments.append(e)
        
        db.session.add(flag)
        db.session.commit()

        new_flag_signal.send(self, message=flag.id)
        return flag

    def change_flag_stauts_to(self, id: str, status: bool) -> Flag:
        flag = Flag.query.get(id)
        flag.active = status

        db.session.add(flag)
        db.session.commit()

        flag_status_signal.send(self, message={"id": flag.id, "status": status})
        return flag
    

def subscribe_new_flag_event(sender, **extra):
    print(f"Received event from {sender}: {extra['message']}")

def subscribe_flag_status_change(sender, **extra):
    print(f"Flag status change: {extra['message']}")

new_flag_signal.connect(subscribe_new_flag_event)
flag_status_signal.connect(subscribe_flag_status_change)