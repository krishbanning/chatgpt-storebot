import json
import os

DB_FOLDER = "json_db"
os.makedirs(DB_FOLDER, exist_ok=True)

def get_db(name):
    path = f"{DB_FOLDER}/{name}.json"
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({}, f)
    return json.load(open(path))

def save_db(name, data):
    path = f"{DB_FOLDER}/{name}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
