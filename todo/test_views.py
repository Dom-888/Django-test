from django.test import TestCase
from .models import Item # Importa Item per poterlo testare con edit_item

# Testare ogni singola funzione in views.py

class TestViews(TestCase):

    def test_get_todo_list(self):
        # Test the http response 
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Confirm that the view uses the correct template
        self.assertTemplateUsed(response, 'todo/todo_list.html')


    def test_get_add_item_page(self):
         # Test the http response 
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)

        # Confirm that the view uses the correct template
        self.assertTemplateUsed(response, 'todo/add_item.html')


    def test_get_edit_page(self):
        item = Item.objects.create(name='my_item') # Crea un'istanza di item al fine di testare l'url di edit_item

        # Test the http response 
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)

        # Confirm that the view uses the correct template
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
         # Test the http response 
        response = self.client.post('/add', {'name': 'my_item'}) # In questo caso si aggunge all'url un item fittizio per testare la risposta

        # Conferma di ritorno alla home page ad avvenuta operazione
        self.assertRedirects(response, '/')


    def test_can_delete_list(self):
        item = Item.objects.create(name='my_item') # Crea un'istanza di item al fine di testare l'url 

        # Test the http response 
        response = self.client.get(f'/delete/{item.id}')
        
        # Conferma di ritorno alla home page ad avvenuta operazione
        self.assertRedirects(response, '/')        

        # Controlla se my_item è ancora presente nel database
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)


    def test_can_toggle_item(self):
        item = Item.objects.create(name='my_item', done='True') # Crea un'istanza di item con done='True' al fine di testare l'url 
        
        # Test the http response 
        response = self.client.get(f'/toggle/{item.id}')

        # Conferma di ritorno alla home page ad avvenuta operazione
        self.assertRedirects(response, '/')

        # Conferma che item.done ritorna 'False'
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)


    def test_can_edit_item(self):
        item = Item.objects.create(name='my_item') # Crea un'istanza di item 

        # Test the http response e modifica il nome dell'item
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})

        # Conferma di ritorno alla home page ad avvenuta operazione
        self.assertRedirects(response, '/')

        # Conferma che il nome è stato modificato
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')