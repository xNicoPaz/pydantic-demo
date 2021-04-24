import os


def get_region():
    return os.environ.get("AWS_REGION", "local")