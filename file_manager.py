from pathlib import Path

def create_users_folder():

    folder = Path("users")
    folder.mkdir(exist_ok=True)

    return folder 

files = {
    "user1": '{"username": "Mark", "age": 22, "email": "mark@example.com"}',
    "user2": '{"username": "Sarh", "age": 25, "email": "sarh@example.com"}'
}

def create_users_file(files, folder):

    for filename, content in files.items():
        file_path = filename / folder
        file_path.write_text(content, encoding="utf-8") 
    return None