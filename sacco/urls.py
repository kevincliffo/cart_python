from django.urls import path
from . import views

app_name = 'sacco'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('add_users/', views.add_users, name='add_users'),
    path('members/', views.members, name='members'),
    path('add_members/', views.add_members, name='add_members'),
    path('members_profile/<memberid>', views.members_profile, name='members_profile'),
    path('own_profile/', views.own_profile, name="own_profile"),
    path('next_of_kins/', views.next_of_kins, name='next_of_kins'),
    path('contributions/', views.contributions, name='contributions'),
    path('add_contributions/', views.add_contributions, name='add_contributions'),
    path('add_single_contribution/<memberid>', views.add_single_contribution, name="add_single_contribution"),
    path('add_contribution/', views.add_contribution, name="add_contribution"),
    path('tickets/', views.tickets, name='tickets'),
    path('loanapplications/', views.loanapplications, name='loanapplications'),
    path('tickets/', views.tickets, name='tickets'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
    path('read_ticket/<id>/<ticketread>', views.read_ticket, name="read_ticket"),
    path('ticket_create/', views.ticket_create, name="ticket_create"),
    path('my_settings/', views.my_settings, name="my_settings"),
    path('settings_update/<id>', views.settings_update, name="settings_update"),
    path('add_setting_to_db', views.add_setting_to_db, name="add_setting_to_db"),
    path('update_delete_setting', views.update_delete_setting, name="update_delete_setting"),
]