from django.urls import path
from . import views

app_name = 'sacco'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('add_users/', views.add_users, name='add_users'),
    path('members/', views.members, name='members'),
    path('add_members/', views.add_members, name='add_members'),
    path('members_profile/<memberid>', views.members_profile, name='members_profile'),
    path('tickets/', views.tickets, name='tickets'),
    path('loanapplications/', views.loanapplications, name='loanapplications'),
]