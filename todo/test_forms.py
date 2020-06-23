from django.test import TestCase
from .forms import ItemForm # Importa la classe da testare dal rispettivo file

# Create your tests here.

class TestItemForm(TestCase):

    # Controlla che il campo name non venga lasciato vuoto
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.') # Controlla che il primo errore riportato in caso di campo vuoto sia uguale a 'This field is required.'

    # Controlla che non vengano lanciati errori se il campo 'done' viene lasciato vuoto
    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Prova nome'})
        self.assertTrue(form.is_valid())

    # Controlla che i campi del form siano 'name' e 'done', in quest'ordine
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm() # Crea una nuova istanza di form
        self.assertEqual(form.Meta.fields, ['name', 'done']) # Controlla che i campi del form appena creato siano quelli giusti

