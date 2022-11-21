from django.contrib import admin
from .models import Post,comentario

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ('title','slug','contenido')

    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post,PostAdmin)
admin.site.register(comentario)