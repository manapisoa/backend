from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('transaction/',views.TransactionListCreateView.as_view()),
    path('transaction/<uuid:id>',views.RetieveUpdateDestroyView.as_view()) ,
    path('create/',views.create_notif),
    path('list/',views.list_notif)
]