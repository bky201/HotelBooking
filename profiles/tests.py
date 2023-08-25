from django.test import TestCase
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    """
    Test Profile app
    """

    def setUp(self):
        """Setup test"""
        username = "bookadmin"
        password = "Add12345"
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username, password=password, is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

    def test_profile_page(self):
        """Test profile page renders correct page"""
        response = self.client.get("/profiles/user/1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_edit_profile_page(self):
        "Test edit profile for user"
        response = self.client.get("/profiles/edit/1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile_form.html")
