import json
import time

user = {
    "id": 1,
    "name": "andy",
    "age": 11,
    "address": "shanghai",
    "married": True,
    "hobbies": ["music", "book", "TV"],
    "createdAt": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
}

json_str = json.dumps(user)
print(json_str)
user = json.loads(json_str)
print(user)

users = [
    {
        "id": 1,
        "name": "小明",
        "age": 11,
        "address": "上海",
        "married": True,
        "hobbies": ["music", "book", "TV"],
        "createdAt": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    },
    {
        "id": 2,
        "name": "小红",
        "age": 12,
        "address": "北京",
        "married": False,
        "hobbies": ["play", "football", "TV"],
        "createdAt": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }
]
json_str = json.dumps(users)
print(json_str)
users = json.loads(json_str)
print(users)
