from django.shortcuts import render
from app.models import Card
from django.views.generic import ListView

class IndexView(ListView):
    model = Card
    template_name = "app/index.html"
    context_object_name = "cards"
