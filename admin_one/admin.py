from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'Finseva Administration'
admin.site.unregister(Group)
admin.site.site_title = 'Finseva Administration'