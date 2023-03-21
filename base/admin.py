from django.contrib import admin
from .models import Word, Time, Mistake, BannerClick

admin.site.register(Word)
admin.site.register(Time)
admin.site.register(Mistake)
admin.site.register(BannerClick)