from datetime import datetime


def get_current_ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")