import unittest
from datetime import datetime
from taller_test.core import api_activities as act


class ApiRequestsActivities(unittest.TestCase):
    now = datetime.now()

    def test_get_all_activities(self):
        self.response = act.get_all_activities()

    def test_get_activity(self, id):
        self.response = act.get_activity(id)

    def test_create_activity(self, id, nombre):
        self.response = act.create_activity(id, nombre, self.now, True)

    def test_update_activity(self, id, nombre):
        self.response = act.create_activity(id, nombre, self.now, True)

    def test_delete_activity(self, id):
        self.response = act.delete_activity(id)

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)


if __name__ == '__main__':
    unittest.main()
