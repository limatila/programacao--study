from django.contrib import admin
from .models import *
from .utils import modelFormatters
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Receita)
class CategoryAdmin(admin.ModelAdmin):
    pass