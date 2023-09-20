from django.db import models

# Create your models here.


class Author(models.Model):

    name = models.CharField(unique=True, max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Poll(models.Model):
    name = models.CharField(unique=True,max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE,related_name='poll')

    def __str__(self):
        return self.name

