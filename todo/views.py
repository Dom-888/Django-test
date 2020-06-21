from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.

def get_todo_list(request):
    items = Item.objects.all() # Contains the whole table
    context = { # Separate the table object in a dictionary
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

def add_item(request):
    if request.method == 'POST': # Solo se questa funzioni è chiamata con il POST method, in questo cas cliccando su "Add item"
        form = ItemForm(request.POST)
        if form.is_valid(): # Se tutti i campi richiesti sono stati compilati
            form.save()
        return redirect("get_todo_list") # Non funziona, why?

    # Se chiamata con GET si limita a generare il form
    form = ItemForm()
    context = {
        'form': form
    }

    return render(request, 'todo/add_item.html', context)