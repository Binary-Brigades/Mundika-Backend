from django.contrib import admin

from .models import Alumni

admin.site.site_header = "Mundika Administration"
admin.site.site_title = "Mundika Admin Portal"
admin.site.index_title = "Welcome to Mundika Admin Portal"

admin.site.register(Alumni)
