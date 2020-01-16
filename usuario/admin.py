from django.contrib import admin
from usuario.models import Pessoa

from .models import *
# Register your models here.
admin.site.register(Pessoa)