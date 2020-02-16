from flask import Flask, request
from flask_testing import TestCase
from app import APP

import unittest
import flask_testing


class MyTest(TestCase):

    def create_app(self):

        APP.config['TESTING'] = True
        return APP

    def test_index(self):
        with APP.test_client() as c:
            rv = c.get('/')
            self.assertEquals(rv.status, '200 OK')

    def test_assert_index_template_used(self):
        with APP.test_client() as c:
            rv = c.get('/')
            self.assert_template_used('pages/index.html')

    def test_assert_recipies_template_used(self):
        with APP.test_client() as c:
            rv = c.get('/recipes')
            self.assert_template_used('pages/recipies.html')


if __name__ == '__main__':
    unittest.main()