from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .utils import modelFormatters as formatters

# Create your models here.

#1 User to Many Receitas
#?to costumize..?

#1 Category to Many Receitas
class Category(models.Model):
    idCategory = models.AutoField(primary_key=True)
    imageCategory = models.ImageField(upload_to="category-covers/", default="/category-covers/default.jpg")

    class CategoryTypes(models.TextChoices): #? Estou errando? eu poderia dar acesso para criar as categorias sem precisar mudar o código bruto.
        #Basics
        BREAKFAST = '1', _('Café da manhã')
        LUNCH = '2', _('Almoço')
        SNACK = '3', _('Lanche')
        DINNER = '4', _('Jantar')
        #More types
        APPETIZER = '101', _('Apelitivo')
        VEGETARIAN = '102', _('Vegetariano')
        VEGAN = '103', _('Vegano')
        OTHERS = '50', _('Outros')

    categoryType = models.CharField(choices=CategoryTypes.choices,
                                    default=CategoryTypes.OTHERS,
                                    max_length=15,
                                    unique=True)

    #Exibição - Admin
    def __str__(self) -> str:
        return formatters.formatCategoryName(self)


class Receita(models.Model):
    idPage = models.AutoField(primary_key=True)
    titleReceita = models.CharField(max_length=150)
    likes = models.IntegerField(default=0)
    imageReceita = models.ImageField(upload_to="receita-covers/",
                                     editable=True)
    publicationDate = models.DateField(auto_now_add=True,
                                       null=False,
                                       blank=False,
                                       editable=False)
    descriptionResumed = models.TextField(max_length=80)

    description = models.TextField(max_length=3000)
    # tempo de preparo
    preparationTimeUnit_Values = {
        'minutos': 'minutos',
        'horas': 'horas',
        'dias': 'dias',
        'meses': 'meses'
    }
    preparationTime = models.IntegerField()  #máximo 1 mês em minutos
    preparationTimeUnit = models.CharField(max_length=7,
                                           choices=preparationTimeUnit_Values,
                                           default='minutos')

    #Foreigns
    userSubmitted = models.ForeignKey(User,
                                      on_delete=models.CASCADE,
                                      null=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)

    #Exibição - Admin
    def __str__(self) -> str:
        return formatters.formatReceitaName(self)
