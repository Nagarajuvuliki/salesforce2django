from django.contrib import admin
from salestodjango import models

admin.site.register(models.Account)
admin.site.register(models.SfUsers)
admin.site.register(models.Contact)