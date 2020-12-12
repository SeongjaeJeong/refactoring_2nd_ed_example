import json


def import_json_file(path: str) -> dict:
    with open(path, "r") as json_invoice:
        result = json.load(json_invoice)

    return result