from django.shortcuts import render

# Create your views here.
from django.views import View

from baza.models import Person


def index(request):
    return render(request, "base.html", {'title': 'dupa'})


def person_function_view(request):
    error = ""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if first_name != "" and last_name != "":
            Person.objects.create(first_name=first_name, last_name=last_name)
        else:
            error = "nie moze być wartości pustej"
    persons = Person.objects.all()
    context = {'persons': persons, "error":error}
    http_response = render(request, "persons.html", context)
    return http_response

class PersonView(View):

    def get(self, request):
        persons = Person.objects.all()
        context = {'persons': persons,}
        http_response = render(request, "persons.html", context)
        return http_response

    def post(self, request):
        error = ""
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if first_name != "" and last_name != "":
            Person.objects.create(first_name=first_name, last_name=last_name)
        else:
            error = "nie moze być wartości pustej"
        persons = Person.objects.all()
        context = {'persons': persons, "error": error}
        http_response = render(request, "persons.html", context)
        return http_response

