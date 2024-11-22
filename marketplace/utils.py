from datetime import datetime
import os
import uuid


def custom_file_name(instance, file_name):
    name, ext = os.path.splitext(file_name)
    upload_datetime = datetime.now().strftime("%Y%m%d%H%M")
    name = uuid.uuid4()
    return os.path.join("images", f"{upload_datetime}-{name}{ext}")
