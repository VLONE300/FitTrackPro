from django.contrib import admin

from users.models import CustomUser, Trainer

admin.site.register(CustomUser)
admin.site.register(Trainer)
