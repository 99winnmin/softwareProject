from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profiles)
admin.site.register(Portfolios)
admin.site.register(PortfolioComments)
admin.site.register(ProfileSubscribeList)
admin.site.register(PortfolioLikeList)

admin.site.register(Image)
