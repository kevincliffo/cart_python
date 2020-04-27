from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import *
import datetime

def index(request):
	context = {}
	return render(request, 'sacco/index.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('sacco:dashboard')

    else:
        form = AuthenticationForm()
    return render(request, 'sacco/index.html', {'form':form})

def dashboard(request):
	context = {'userscount':4,
               'memberscount':4,
               'loanapplicationscount':4,
               'ticketscount':4}
	return render(request, 'sacco/dashboard.html', context)

def users(request):
	context = {'userscount':4}
	return render(request, 'sacco/users.html', context)

def add_users(request):
	context = {}
	return render(request, 'sacco/users_add.html', context)    

def members(request):
    members = Member.objects.all()
    context = {'login_type':'user',
               'members': members}
    return render(request, 'sacco/members.html', context)

def generatememberno():
    id = Member.objects.values('id').order_by('-id').first()
    if id == None:
        memberid = 0
    else:
        memberid = id['id']
        
    print('memberid : ' + str(memberid))
    memberid = int(str(memberid)) + 1

    prefix = 'UNGI'
    currentyear = str(datetime.datetime.now().year)
    #UNGI-2020-000003
    memberno = prefix \
             + '-' \
             + currentyear \
             + '-' \
             + str(memberid).zfill(6)

    return memberno

def add_members(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        inputEmail = request.POST.get('inputEmail')
        inputPassword = request.POST.get('inputPassword')
        mobileNumber = request.POST.get('mobileNumber')
        idNumber = request.POST.get('idNumber')
        memberType = request.POST.get('memberType')
        gender = request.POST.get('gender')
        nextofkinName = request.POST.get('nextofkinName')
        nextofkinmobileNumber = request.POST.get('nextofkinmobileNumber')
        nextofkinRelationship = request.POST.get('nextofkinRelationship')

        memberno = generatememberno()
        Member.objects.create(MemberNo = memberno, FirstName=firstname, LastName=lastName, Email=inputEmail, Password=inputPassword, MobileNo=mobileNumber,
        IdNumber=idNumber, MemberType=memberType, MemberGender=gender, NextOfKinFullName=nextofkinName, NextOfKinMobileNo=nextofkinmobileNumber, 
        NextOfKinRelationship=nextofkinRelationship)
        return redirect('sacco:add_members')
    else:
        context = {}
        return render(request, 'sacco/members_add.html', context) 

def members_profile(request, memberid):
	context = {}
	return render(request, 'sacco/members_profile.html', context)

def loanapplications(request):
	context = {'loanapplicationscount':4}
	return render(request, 'sacco/dashboard.html', context)

def tickets(request):
	context = {'ticketscount':4}
	return render(request, 'sacco/dashboard.html', context)    