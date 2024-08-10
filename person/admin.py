from django.contrib import admin
from .models import Person

models_list = [Person]
admin.site.register(models_list)
# Register your models here.
