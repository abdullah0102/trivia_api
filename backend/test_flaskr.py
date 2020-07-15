import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"#trivia_test
        self.database_path = "postgres://{}/{}".format('postgres:1234@127.0.0.1:5432', self.database_name)
        setup_db(self.app, self.database_path)
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_all_categories(self): #done
        x = self.client().get('/category')
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["category"]))

    def test_get_paginated_question(self): #done
        x = self.client().get('/question?page=1')
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["question"]))
        self.assertTrue(data["total_question"])
        self.assertTrue(len(data["Category"]))

    def test_get_paginated_question_404(self):#done
        x = self.client().get('/question?page=1000000')
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not found")

    def test_delete_question(self):#done
        x = self.client().delete('/question/177')
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_delete_question_404(self):#done
        x = self.client().delete('/question/100000000')
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not found")

    def test_addQuestion(self):#done
        insert_data = {
            'question': 'If A and B together can complete a piece of work in 15 days and B alone in 20 days, in how many days can A alone complete the work?',
            'answer': '60',
            'category': "Science",
            'difficulty': 1
        }
        x = self.client().post('/question', json=insert_data)
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_addQuestion_422(self):#done
        insert_data = {
            'question': 'test',
            'answer': 'test'
        }
        x = self.client().post('/question', json=insert_data)
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")


    def test_search_questions(self):
        insert_data = {
            'search_term': 'x',
        }
        x = self.client().post('/questionSearch', json=insert_data)
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["question"]))
        self.assertTrue(data["count"])

    def test_search_questions_422(self):
        insert_data = {
            'search_term': None,
        }
        x = self.client().post('/questionSearch', json=insert_data)
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_search_questions_422(self):
        insert_data = {
            'search_term': None,
        }
        x = self.client().post('/questionSearch', json=insert_data)
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_getQuestionByCategory(self):
        x = self.client().get('/category/29/question')
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["questions"]))

    def test_getQuestionByCategory_404(self):
        x = self.client().get('/category/1000/question')
        data = json.loads(x.data)
        self.assertEqual(x.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not found")

    def test_play_quiz(self):
        insert_data = {
            'previous_questions': [],
            'category': 'Science'
        }
        res = self.client().post('/Quiz', json=insert_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])

    def test_play_quiz_422(self):
        insert_data = {}
        res = self.client().post('/Quiz', json=insert_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_play_quiz_404(self):
        insert_data = {
            'previous_questions': [Question.query.filter_by(category = "Science").order_by('id').all()],
            'category': 'Science'
        }
        res = self.client().post('/Quiz', json=insert_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not found")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()