from xml.etree.ElementInclude import include
from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_todolist, name='add_todolist'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('task-changes/<int:id>', task_changes, name='task_changes'),
    path('json/', get_json, name="get_json"),
    path('add/', add_todolist_ajax, name="add_todolist_ajax" )
]