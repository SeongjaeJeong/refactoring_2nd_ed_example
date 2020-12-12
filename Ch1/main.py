from utils import import_json_file
from statement import statement

if __name__ == "__main__":
    invoice = import_json_file("invoices.json")
    plays = import_json_file("plays.json")

    result = statement(invoice[0], plays)

    print(result)
