from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'id')
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'nivel')
    list_display_links = ('nome', 'codigo')
    search_fields = ('nome', 'codigo', 'nivel')
    list_per_page = 20

admin.site.register(Curso, Cursos)