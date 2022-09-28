import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from todolist.models import ToDoList
from todolist.forms import ToDoListForms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    if request.user.is_authenticated:
        todolist = ToDoList.objects.filter(user=request.user)
        context = {
            'list_kerjaan' : todolist,
            'user_name' : request.user.username,
            'last_login': request.COOKIES['last_login'],
        }
        return render(request, 'todolist.html', context)
    
    else:
        return redirect('todolist:login')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def add_todolist(request):
    if request.user.is_authenticated:
        form = ToDoListForms(request.POST)
        if request.method == 'POST' and form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task_baru = ToDoList.objects.create(title=title, description=description,
                                                user=request.user, date=datetime.date.today())
            return redirect('todolist:show_todolist')
        
        context = {
            'form' : form,
        }
        return render(request, 'newtodolist.html', context)
    else:
        return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def task_changes(request, id):
    task_todolist = ToDoList.objects.get(id=id)
    task_todolist.is_finished = not task_todolist.is_finished
    task_todolist.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')  
def delete_task(request, id):
    task_todolist = ToDoList.objects.get(id=id)
    task_todolist.delete()
    return redirect('todolist:show_todolist')