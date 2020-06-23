from django.test import TestCase
from .models import Item 

class TestModels(TestCase):

    # Crea un istanza di item fittizia per verificare my_item.done = "False", ovvero la condizione di default
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name="my_item")
        self.assertFalse(item.done)

    # Questo test è stato aggiunto per completare la coverage. Verifica che lo str(my_item) ritorna il suo nome (e quindi?)
    def test_item_string_method_return_name(self):
        item = Item.objects.create(name='my_item')
        self.assertEqual(str(item), 'my_item')
