import json
from pathlib import Path

def create_users_folder():
    folder = Path("users") 
    folder.mkdir(exist_ok=True)

    return folder

def create_user_files(users_data, users_folder):
    for filename, data in users_data.items():
        file_path = users_folder / filename #عشان المفروض من الدايه نحدد اسم الملف مع الامتداد بدل نكتبه هنا


        file_path.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8"
        )
