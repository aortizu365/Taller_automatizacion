import unittest
from datetime import datetime
from taller_test.core import api_books as act


class ApiRequestsBooks(unittest.TestCase):
    now = datetime.now()

    def test_get_all_books(self):
        self.response = act.get_all_books()

    def test_get_book(self, id):
        self.response = act.get_book(id)

    def test_create_book(self, id, nombre):
        self.response = act.create_book(id, nombre, self.now, True)

    def test_update_book(self, id, nombre):
        self.response = act.create_book(id, nombre, self.now, True)

    def test_delete_book(self, id):
        self.response = act.delete_book(id)

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)


if __name__ == '__main__':
    unittest.main()
