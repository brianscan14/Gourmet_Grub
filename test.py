from flask import Flask, request
from flask_testing import TestCase

import unittest
import flask_testing


app = Flask(__name__)


class MyTest(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_index(self):
        with app.test_client() as c:
            rv = c.get('/')
            self.assertEqual(rv.status, '200 ok')


if __name__ == '__main__':
    unittest.main()