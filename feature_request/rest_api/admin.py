from django.contrib import admin

from .models import (Clients,
                     ProductAreas,
                     FeatureRequests,
                     )

admin.site.register(Clients)
admin.site.register(ProductAreas)
admin.site.register(FeatureRequests)

