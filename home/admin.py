from django.contrib import admin
from .models import PricePlan,Service,Portfolio,Post,Order,Comments

for a in [PricePlan,Service,Portfolio,Post,Order,Comments]:
    admin.site.register(a)