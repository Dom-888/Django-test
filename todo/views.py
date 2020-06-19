from django.shortcuts import render, HttpResponse, redirect
from .models import Item

# Create your views here.

def get_todo_list(request):
    items = Item.objects.all() # Contains the whole table
    context = { # Separate the table object in a dictionary
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

def add_item(request):
    if request.method == 'POST': # Solo se questa funzioni è chiamata con il POST method
        name = request.POST.get("item_name") # Recupera il nome dal form
        done = 'done' in request.POST # Recupera la booleana dal form
        Item.objects.create(name=name, done=done) # Crea l'object attraverso la Item class e gli assegni i valori attraverso le variabil i appena create

        return redirect("get_todo_list") # Non funziona, why?
    return render(request, 'todo/add_item.html')