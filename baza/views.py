from django.shortcuts import render

# Create your views here.
from baza.models import Person


def index(request):
    return render(request, "base.html" , {'title':'dupa'})


def person_function_view(request):
    persons = Person.objects.all()
    context = {'persons':persons, 'title':'Person'}
    http_response = render(request, "persons.html", context)
    return http_response