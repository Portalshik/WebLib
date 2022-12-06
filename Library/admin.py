from django.contrib import admin

# Register your models here.
from .models import Categories, Additions, Authors, Tags, Books

admin.site.register(Categories)
admin.site.register(Additions)
admin.site.register(Authors)
admin.site.register(Tags)
admin.site.register(Books)
