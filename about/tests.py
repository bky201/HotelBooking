from django.test import TestCase


class TestViews(TestCase):
    """ Test About app"""
    def test_about_page(self):
        """ Test about page renders correct page """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')