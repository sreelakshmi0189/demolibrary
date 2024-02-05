from django.db import models

# Create your models here.

class Book(models.Model):  #DB table definition in Django
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    price=models.IntegerField()
    pdf=models.FileField(upload_to="books/pdf")
    cover=models.ImageField(upload_to="books/cover",null=True,blank=True)
    def __str__(self):
        return self.author