from django.urls import path
from . import views

urlpatterns = [
    path('board/', views.home, name = 'home'),
    path('show_write_form/', views.show_write_form),
    path('DoWriteBoard/', views.DoWriteBoard),
    path('listSpecificPageWork/', views.listSpecificPageWork),
    path('view/', views.viewWork, name = 'viewWork'),
]