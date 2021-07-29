from django.contrib import admin
from .models import BlankContent, NewBlank

# Register your models here.
admin.site.register(NewBlank)
admin.site.register(BlankContent)