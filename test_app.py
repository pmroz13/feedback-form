from app import app
import unittest


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app_test = app.test_client(self)

    def test_feedback(self):
        resp = self.app_test.get('/feedback-form', content_type='html/text')
        self.assertEqual(resp.status_code, 200)

    def test_thank(self):
        resp = self.app_test.get('/thank-you', content_type='html/text')
        self.assertEqual(resp.status_code, 200)

    def test_feedback_correct(self):
        resp = self.app_test.post('/feedback-form', data=dict(title='test', summary='correct feedback'),
                                  follow_redirects=True)
        self.assertIn(b'Thank You!', resp.data)

    def test_feedback_incorrect(self):
        resp = self.app_test.post('/feedback-form', data=dict(title='', summary='incorrect feedback'),
                                  follow_redirects=True)
        self.assertIn(b'Feedback form', resp.data)
