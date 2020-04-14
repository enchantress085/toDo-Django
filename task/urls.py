from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('updatelist/<str:pk>', views.updateTask, name="updateTask"),
    path('delete/<str:pk>', views.deleteTask, name="deleteTask"),
]