from logs.models import Log


def logs(log_type='debug', name=None, description=None):
    log = Log(log_type=log_type, name=name, description=description)
    log.save()

