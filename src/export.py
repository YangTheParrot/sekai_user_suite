import json 
from crypto.APIManager import unmsgpack
    
# export into json file
def export_user_suite(file: str, server: str):
    data = open(file, "rb").read()
    with open(file + ".json", "w", encoding="utf-8") as out:
        unpacked = unmsgpack(data, server)
        json.dump(unpacked, out, indent=4, ensure_ascii=False)