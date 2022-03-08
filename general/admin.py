from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from general.models import JobPost, Category, Tag, Location

# Register your models here.

admin.site.register(JobPost)
admin.site.register(Tag)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Location, MPTTModelAdmin)
