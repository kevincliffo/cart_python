from django.contrib import admin
from . models import Financial, Member, User, Ticket, Setting

admin.site.register(Financial)
admin.site.register(Member)
admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Setting)
