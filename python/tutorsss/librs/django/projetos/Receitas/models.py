from django.db import models

# Create your models here.
class Receita(models.Model):
    idPage = models.IntegerField(primary_key=True)
    titleReceita = models.CharField(max_length=150)
    imageReceita = models.ImageField(upload_to="static/Receitas/imgs/%d/%m/%Y", editable=True)
    userName = models.CharField(max_length=100)
    userEmail = models.CharField(max_length=60)
    publicationDate = models.DateField(auto_now_add=True)
    descriptionResumed = models.TextField(max_length=80)
    description = models.TextField(max_length=3000)

    # tempo de preparo
    preparationTimeUnit_Values = {'minutos': 'minutos', 
                                  'horas': 'horas', 
                                  'dias': 'dias', 
                                  'meses': 'meses'}
    preparationTime = models.IntegerField() #máximo 1 mês em minutos
    preparationTimeUnit = models.CharField(max_length=7, 
                                           choices=preparationTimeUnit_Values, 
                                           default='minutos')

class User(models.Model):
    idUser = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    creationDateTime = models.DateTimeField(auto_now_add=True)
    #? recipesCreatedIDs