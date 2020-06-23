from django.test import TestCase
from .models import Item 

# Crea un istanza di item fittizia per verificare my_item.done = "False", ovvero la condizione di default

class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name="my_item")
        self.assertFalse(item.done)