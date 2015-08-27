from django.contrib import admin

from .models import (Client,
                     ProductArea,
                     FeatureRequest,
                     )

class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']})
        ]


admin.site.register(Client, ClientAdmin)


class ProductAreaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']})
        ]

    
admin.site.register(ProductArea, ProductAreaAdmin)


class FeatureRequestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('description', {'fields': ['description']}),
        ('Client URI', {'fields': ['client_uri']}),
        ('Client Priority', {'fields': ['client_priority']}),
        ('Target Date', {'fields': ['target_date']}),
        ('Ticket URI', {'fields': ['ticket_uri']}),
        ('Product Area URI', {'fields': ['product_area_uri']})
        ]
admin.site.register(FeatureRequest)

