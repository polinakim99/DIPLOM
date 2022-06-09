from django.contrib import admin
from .models import Category, Perform, PerformShots, News, People, Reviews, Comments, Seat, SessionSeat, Session, \
    CustomUser
# Register your models here.


class PeopleAdmin(admin.ModelAdmin):
    list_display = ("surname", "name")


class CommentAdmin(admin.ModelAdmin):
    """ Комментарии
    """
    list_display = ('username', 'perform', 'created', 'moderation')


admin.site.register(Comments, CommentAdmin)
admin.site.register(Category)
admin.site.register(Seat)
admin.site.register(SessionSeat)
admin.site.register(Session)
admin.site.register(CustomUser)
admin.site.register(People, PeopleAdmin)
admin.site.register(Perform)
admin.site.register(PerformShots)
admin.site.register(Reviews)
admin.site.register(News)

