import unittest
import json
from app.api.MyPyCalc import app

class MyPyCalcTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.api_url = 'http://localhost:5000'  # Change the port to 5000

    def test_add(self):
        data = {'num1': 5, 'num2': 3}
        response = self.app.post('/add', data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['result'], 8)

    def test_subtract(self):
        data = {'num1': 10, 'num2': 4}
        response = self.app.post('/subtract', data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['result'], 6)

    def test_missing_data(self):
        data = {'num1': 5}  # Missing 'num2'
        response = self.app.post('/add', data=json.dumps(data), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['error'], 'Missing data')

if __name__ == '__main__':
    unittest.main()
