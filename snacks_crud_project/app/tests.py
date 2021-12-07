from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snacks


class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.thing = Snacks.objects.create(
            title="coffee3", description='coffee3', purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.thing), "pickle")

    def test_thing_content(self):
        self.assertEqual(f"{self.thing.title}", "coffee3")
        self.assertEqual(f"{self.thing.description}", "coffee3")
        self.assertEqual(self.thing.purchaser, 'admin')

    def test_snacks_list_view(self):
        response = self.client.get(reverse("snacks_list"))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "coffee3")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snacks_detail_view(self):
        response = self.client.get(reverse("snacks_detail", args="1"))
        # no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(no_response.status_code, 404)
        # self.assertContains(response, "Reviewer: tester")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snacks_create_view(self):
        response = self.client.post(
            reverse("snacks_create"),
            {
                "title": "ice",
                "description": "gfggg",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snacks_create", args="2"))
        # self.assertContains(response, "Details about Rake")

    def test_snacks_update_view_redirect(self):
        response = self.client.post(
            reverse("snacks_update", args="1"),
            {"title": "Updated name","description":"3jhgfdsa","purchaser":self.user.id}
        )

        self.assertRedirects(response, reverse("snacks_detail", args="1"))

    def test_snacks_delete_view(self):
        response = self.client.get(reverse("snacks_delete", args="1"))
        self.assertEqual(response.status_code, 200)