"""kino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from baza import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path("persons/", views.person_function_view, name='persons'),
    path("movie/", views.MovieView.as_view(), name='movie'),
    path("role/", views.RoleView.as_view(), name='role'),
    path("add_role/", views.AddRoleView.as_view(), name='add_role'),
    path("persons_by_class/", views.PersonView.as_view(), name='persons_by_class'),
    path("edit_person/<int:id>/", views.PersonEditView.as_view(), name='edit_person'),
    path("delete_person/<int:id>/", views.DeletePersonView.as_view(), name='delete_person'),
]
