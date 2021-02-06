from django.test import TestCase
from django.urls import reverse


class LandingPageTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")
