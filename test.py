from flask import Flask, request, url_for
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

    def test_assert_add_template_used(self):
        with APP.test_client() as c:
            rv = c.get('/add')
            self.assert_template_used('pages/addrecipe.html')

    def test_assert_cuisines_template_used(self):
        with APP.test_client() as c:
            rv = c.get('/cuisines')
            self.assert_template_used('pages/cuisines.html')

    def test_assert_meals_template_used(self):
        with APP.test_client() as c:
            rv = c.get('/meals')
            self.assert_template_used('pages/findmeals.html')

    def test_add_ok(self):
        with APP.test_client() as c:
            rv = c.post('/add', follow_redirects=True, data=(
                'recipe_name': 'new recipe',
                'recipe_prep': 'step',
                'recipe_desc': 'description of recipe',
                'cuisine_name': 'cuisine',
                'image': 'url string',
                'ingredients': 'ingredients list',
                'meal_type': 'lunch',
                'calories': '55',
                'duration': '66',
                'views': '1'
            ))
            self.assert_template_used('pages/thankyou.html')

if __name__ == '__main__':
    unittest.main()