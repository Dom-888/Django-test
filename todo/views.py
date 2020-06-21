from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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

def edit_item(request, item_id):
    # Ottiene l'oggetto dal database e lo assegna alla variabile item
    item = get_object_or_404(Item, id=item_id )
    if request.method == 'POST': # Solo se questa funzioni è chiamata con il POST method, in questo cas cliccando su "Add item"
        form = ItemForm(request.POST, instance=item)
        if form.is_valid(): # Se tutti i campi richiesti sono stati compilati
            form.save()
            return redirect("get_todo_list") # Non funziona, why?

    # Compila il form con la variabile item (ovvero l'oggetto estratto dal database)
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)