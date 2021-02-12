from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from baza.models import Person, Movie, Role


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
    context = {'persons': persons, "error": error}
    http_response = render(request, "persons.html", context)
    return http_response


class PersonView(View):

    def get(self, request):
        persons = Person.objects.all()
        context = {'persons': persons, }
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
        return redirect("persons")


class PersonEditView(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        movies = Movie.objects.all()
        return render(request, 'persons.html', {'person': person, 'movies':movies})

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        person.first_name = first_name
        person.last_name = last_name
        person.save()
        return redirect('persons')


class DeletePersonView(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        return render(request, 'persons_delete.html', {'person': person})

    def post(self, request, id):
        odp = request.POST.get('submit')
        if odp == "ok":
            person = Person.objects.get(pk=id)
            person.delete()
        return redirect('persons')

class MovieView(View):

    def get(self, request):
        persons = Person.objects.all()
        movies = Movie.objects.all()
        return render(request, "movie.html", {'persons':persons, 'movies':movies})

    def post(self, request):
        title = request.POST['title']
        year = request.POST['year']
        screenplay_id = request.POST['screenplay']
        director_id = request.POST['director']

        screenplay = Person.objects.get(pk=screenplay_id)
        director = Person.objects.get(pk=director_id)
        m = Movie.objects.create(title=title, year=year, screenplay=screenplay, director=director)
        m.actors.set([1,2,3])
        return redirect('movie')


class RoleView(View):

    def get(self, request):
        persons = Person.objects.all()
        movies = Movie.objects.all()
        return render(request, "role.html", {'persons':persons, 'movies':movies})

    def post(self, request):
        movie = Movie.objects.get(id=request.POST['movie'])
        actor = Person.objects.get(id=request.POST['actor'])
        role = request.POST['role']
        Role.objects.create(movie=movie, person=actor, role=role)
        return redirect('role')

class AddRoleView(View):

    def post(self, request):
        person = Person.objects.get(id = request.POST['person'])
        movie = Movie.objects.get(id=request.POST['movie'])
        role = request.POST['role']
        Role.objects.create(movie=movie, person=person, role=role)
        return redirect('edit_person', person.id)








