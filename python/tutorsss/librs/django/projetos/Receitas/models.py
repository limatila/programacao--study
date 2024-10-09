from django.db import models

# Create your models here.
class receita(models.Model):
    idPage = models.IntegerField(primary_key=True)
    titleReceita = models.CharField(max_length=150)
    imageReceita = models.ImageField(upload_to="static/Receitas/imgs/", editable=True)
    userName = models.CharField(max_length=100)
    userEmail = models.CharField(max_length=60)
    publicationDate = models.DateField(auto_now_add=True)
    description = models.TextField(editable=False, max_length=3000)

class user(models.Model):
    idUser = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    creationDateTime = models.DateTimeField(auto_now_add=True)
    #? recipesCreatedIDs