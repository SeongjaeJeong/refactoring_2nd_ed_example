import unittest
from utils import import_json_file
from statement import statement


class TestStatement(unittest.TestCase):
    def setUp(self):
        self.invoice = import_json_file("invoices.json")
        self.plays = import_json_file("plays.json")

    def test_statement_not_none(self):
        result = statement(self.invoice[0], self.plays)
        self.assertIsNotNone(result)

    def test_statement_correct(self):
        result_expected = (
            "청구 내역 (고객명: BigCo)\n"
            "\tHamlet: $650.0 (55석)\n"
            "\tAs You Like It: $580.0 (35석)\n"
            "\tOthello: $500.0 (40석)\n"
            "총액: $1,730.0\n"
            "적립 포인트: 47점"
        )

        result = statement(self.invoice[0], self.plays)
        self.assertMultiLineEqual(result_expected, result)


if __name__ == "__main__":
    unittest.main()