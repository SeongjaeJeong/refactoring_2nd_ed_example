import json
import os

def import_json_file(path: str) -> dict:
    with open(path, "r") as json_invoice:
        result = json.load(json_invoice)
    
    return result


if __name__ == "__main__":
    invoice = import_json_file('invoices.json')
    plays = import_json_file('plays.json')
