
import urllib.request

from flask import Flask, request
from flask_testing import TestCase, LiveServerTestCase

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
            fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
            self.assertEquals(fhand.status_code, 200)


if __name__ == '__main__':
    unittest.main()