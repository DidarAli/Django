from django.contrib import admin

# Register your models here.


from .models import Kafedra, Predmety

admin.site.register(Kafedra)
admin.site.register(Predmety)