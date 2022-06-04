from django.test import TestCase
from .models import ObjectModel

# Testing the model
class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testthing = ObjectModel.objects.create(name = "test_thing", description="Testing thing")
        testthing.save()


    def test_things_model(self):
        thing = ObjectModel.objects.get(id=1)
        actual_title = thing.name
        self.assertEqual(actual_title, "test_thing")