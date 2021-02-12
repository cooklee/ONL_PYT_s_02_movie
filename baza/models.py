from django.db import models
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="directed_by")
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="writen_by")
    actors = models.ManyToManyField(Person, related_name='roles', through='Role')



class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    role = models.CharField(max_length=128)
