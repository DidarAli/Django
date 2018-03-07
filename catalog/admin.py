from django.contrib import admin

# Register your models here.


from .models import Kafedra, Predmet

admin.site.register(Kafedra)
admin.site.register(Predmet)