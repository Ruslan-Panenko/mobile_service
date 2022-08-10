from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('create/', views.create_task, name='create_task'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('create_invoice/<int:task_id>/', views.create_invoice, name='create_invoice'),

]