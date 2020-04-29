from django.contrib import admin
from . models import Contribution, Member, User, Ticket, Setting

admin.site.register(Contribution)
admin.site.register(Member)
admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Setting)
