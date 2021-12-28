from django.test import TestCase
from django.urls import reverse
# response status code
# template that a view is using

class ThingTests(TestCase):

    def test_snakes_list_status_code(self):
        url = reverse('snakes_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snakes_detail_status_code(self):
        url = reverse('snakes_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snakes_list_template(self):
        url = reverse('snakes_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "_base.html")

    def test_snakes_detail_template(self):
        url = reverse('snakes_detail')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertTemplateUsed(response, "_base.html")