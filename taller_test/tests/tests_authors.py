import unittest
from datetime import datetime
from taller_test.core import api_authors as act


class ApiRequestsAuthors(unittest.TestCase):
    now = datetime.now()

    def test_get_all_authors(self):
        self.response = act.get_all_authors()

    def test_get_author(self, id):
        self.response = act.get_author(id)

    def test_get_libro_author(self, id):
        self.response = act.get_author(id)

    def test_create_author(self, id, nombre):
        self.response = act.create_author(id, nombre, self.now, True)

    def test_update_author(self, id, nombre):
        self.response = act.create_author(id, nombre, self.now, True)

    def test_delete_author(self, id):
        self.response = act.delete_author(id)

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)


if __name__ == '__main__':
    unittest.main()
