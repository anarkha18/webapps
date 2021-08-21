from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact)
# admin.site.register(Post)
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tiny.js',)
