from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MainPageView(TemplateView):
    template_name = "index.html"
    
class ActivityPageView(TemplateView):
    template_name = "activity.html"

class PlanPageView(TemplateView):
    template_name = "plan.html"
    
class RequestPageView(TemplateView):
    template_name = "request.html"