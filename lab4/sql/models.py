from django.db import models

class Book(models.Model):
    id_book = models.CharField(max_length=100)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.id_book
