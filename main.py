import logging
from file_manager import create_users_folder, create_user_files
import json
from pathlib import Path


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s "
)

users_data = {
    "user1.json": {
        "username": "Mark",
        "age": 22,
        "email": "mark@example.com"
    },
    "user2.json": {
        "username": "Sarh",
        "age": 24,
        "email":"sarh@example.com"
    },
    "user3.json": {}
}

folder = create_users_folder()

create_user_files(users_data, folder)


def process_user_file(filename):

    with open(filename, 'r') as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise TypeError("Expected a JSON object.")

    if "username" not in data:
        raise ValueError("Missing a required field 'username'.")

    if "age" not in data:
        raise ValueError("Missing a required field 'age'.")

    if "email" not in data:
        raise ValueError("Missing a required field 'email'.")

    if not isinstance(data["username"], str):
        raise TypeError("Field 'username' should be a string.")

    if not isinstance(data["email"], str):
        raise TypeError("Field 'email' should b a string.")

    if type(data["age"]) is not int:
        raise TypeError("Fild 'age' should be an integer.")

    if data["age"] <= 0:
        raise ValueError("Fild 'age' should be positive.")

    return data



for filename in folder.glob("*.json"):
    try:
        print(process_user_file(filename))
    except FileNotFoundError:
        logging.warning("File was not found: %s", filename)

    except json.JSONDecodeError:
        logging.warning("Invalid JSON format: %s", filename)

    except (TypeError, ValueError) as e:
        logging.warning("Invalid data structure: %s - %s", e, filename)

    else:
        logging.info("The operation was successful! %s", filename)

