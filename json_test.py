import json
import time

user = {
    "id": 1,
    "name": "andy",
    "age": 11,
    "address": "shanghai",
    "marry": True,
    "hobby": ["music", "book", "TV"],
    "createdAt": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
}

json_str = json.dumps(user)
print(json_str)

user = json.loads(json_str)
print(user)
