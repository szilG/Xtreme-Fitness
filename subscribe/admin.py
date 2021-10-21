from django.contrib import admin
from .models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)


admin.site.register(Subscribe, SubscribeAdmin)
