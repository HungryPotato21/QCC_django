from django.urls import path
from main import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name = 'index'),
    path('activity/', views.ActivityPageView.as_view(), name = 'activity'),
    path('plan/', views.PlanPageView.as_view(), name = 'plan'),
    path('request/', views.RequestPageView.as_view(), name = 'request'),
]