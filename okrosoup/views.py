from tkinter.tix import Form
from django.shortcuts import render
from okrosoup.models import todo
# Create your views here.
from django.shortcuts import render
from .forms import todoform 
    
def index(request):
    todo_list = todo.objects.order_by('id')

    form = todoForm() 
    
    context = {'todo_list': todo_list 'form' : form}  
    return render(request, 'todo/index.html', context")
                  
    