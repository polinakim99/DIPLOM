from django.contrib import admin
from .models import Category, Perform, PerformShots, News, People, RatingStar, Rating, Reviews
# Register your models here.


class PeopleAdmin(admin.ModelAdmin):
    list_display = ("surname", "name")


admin.site.register(Category)
admin.site.register(People, PeopleAdmin)
admin.site.register(Perform)
admin.site.register(PerformShots)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(RatingStar)
admin.site.register(News)

