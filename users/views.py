from django.shortcuts import render

from django.views import View

# class EventCreateView(View):
#     template_name = 'index.html'

def index(request):
    return render(request, 'index.html')