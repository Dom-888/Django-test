from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.

def get_todo_list(request):
    items = Item.objects.all() # Contains the whole table
    context = { # Separate the teble object in a dictionary
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)