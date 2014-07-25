from django.contrib import admin

# Register your models here.
import bythebook.models

admin.site.register(bythebook.models.Book)
admin.site.register(bythebook.models.Author)
