import unittest
from utils import import_json_file


class TestImportJson(unittest.TestCase):
    def test_imported_invoice_not_none(self):
        invoice = import_json_file("invoices.json")
        self.assertIsNotNone(invoice)

    def test_imported_plays_not_none(self):
        plays = import_json_file("plays.json")
        self.assertIsNotNone(plays)


if __name__ == "__main__":
    unittest.main()