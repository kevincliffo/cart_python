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
        loginType = request.POST.get('loginType')
        if loginType == 'User':
            request.session['loginType'] = 'user'
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)

                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('sacco:dashboard')
        else:
            memberExists = Member.objects.filter(Email=request.POST.get('username')).filter(Password=request.POST.get('password'))
            
            if memberExists:
                member = Member.objects.get(Email=request.POST.get('username'))
                request.session['memberid'] = member.id
                request.session['email'] = request.POST.get('username')
                request.session['loginType'] = 'member'
                return redirect('sacco:dashboard')


    else:
        form = AuthenticationForm()
    return render(request, 'sacco/index.html', {'form':form})

def logout(reqquest):
    return redirect('sacco:index')

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
    member = Member.objects.get(pk=memberid)
    context = {'member' : member}
    return render(request, 'sacco/members_profile.html', context)
    
def own_profile(request):
    memberId = request.session['memberid']
    member = Member.objects.get(pk=memberId)
    context = {'member' : member}
    return render(request, 'sacco/members_profile.html', context)

def loanapplications(request):
	context = {'loanapplicationscount':4}
	return render(request, 'sacco/dashboard.html', context)

def tickets(request):
	context = {'ticketscount':4}
	return render(request, 'sacco/dashboard.html', context)

def next_of_kins(request):
    members = Member.objects.all().values('id', 'MemberNo', 'FirstName','LastName','NextOfKinFullName','NextOfKinMobileNo','NextOfKinRelationship')
    context = {'login_type':'user',
               'members': members}
    return render(request, 'sacco/next_of_kins.html', context)

def contributions(request):
    contributions = Contribution.objects.all()
    context = {'contributions': contributions}
    return render(request, 'sacco/contributions.html', context)

def add_contributions(request):
    members = Member.objects.all().values('id', 'MemberNo', 'FirstName','LastName','MemberType')
    context = {'members': members}
    return render(request, 'sacco/contributions_add.html', context)
    
def add_single_contribution(request, memberid):
    member = Member.objects.get(pk=memberid)
    months = []
    for i in range(1,13):
        d = datetime.datetime(2020, i, 1)
        month = d.strftime("%B")
        months.append(month)

    context = {'member': member,
               'months':months}
    return render(request, 'sacco/contributions_add_single.html', context)

def convert_string_date_to_date(stringDate):
    dt = datetime.datetime.strptime(stringDate, '%d-%m-%Y')
    return dt

def add_contribution(request):
    if request.method == 'POST':
        name = request.POST.get('firstName') \
             + ' ' \
             + request.POST.get('lastName')

        paymentDate = request.POST.get('paymentDate')
        pd = convert_string_date_to_date(paymentDate)
        transactionDate = datetime.datetime.now()
        paymentMonth = request.POST.get('paymentMonth')
        amount = request.POST.get('amount')
        memberId = request.POST.get('memberId')

        Contribution.objects.create(FullName=name, MemberNo_id=memberId, Amount=amount, TransactionDate=transactionDate,
                                    PaymentDate=pd,PaymentMonth=paymentMonth)

        return redirect('sacco:add_contributions')

def tickets(request):
    try:
        tickets = Ticket.objects.all()
    except Exception as err:
        tickets = []
    context = {'tickets': tickets}
    return render(request, 'sacco/tickets.html', context)

def read_ticket(request, id, ticketread):
    if ticketread == 'False':
        result = Ticket.objects.filter(pk=int(id)).update(TicketRead=1)

    ticket = Ticket.objects.get(pk=1)
    context = {'ticket' : ticket, 'logintype': request.session['loginType']}
    return render(request, 'sacco/ticket_read.html', context)

def my_tickets(request):
    email = request.session['email']
    
    try:
        tickets = Ticket.objects.filter(Sender=email)
    except Exception as err:
        tickets = None
    
    context = {'tickets': tickets}
    return render(request, 'sacco/my_tickets.html', context)

def ticket_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        sender = request.session['email']
        Ticket.objects.create(Title = title, Content=content, Sender=sender, CreatedDate=datetime.datetime.now(), 
                              ReadDate=datetime.datetime.now())
        return redirect('sacco:ticket_create')
    else:
        context = {}
        return render(request, 'sacco/ticket_create.html', context)     

def my_settings(request):
    settings = Setting.objects.all()
    print("request.session['loginType'] :" + str(request.session['loginType']))
    context = {'settings': settings, 'loginType': str(request.session['loginType'])}
    return render(request, 'sacco/settings.html', context)

def add_setting_to_db(request):
    settingkey = request.POST.get('settingKey')
    settingname = request.POST.get('settingName')
    settingvalue = request.POST.get('settingValue')

    Setting.objects.create(SettingKey=settingkey, SettingName=settingname, SettingValue=settingvalue)

    return redirect('sacco:my_settings')

def settings_update(request, id):
    setting = Setting.objects.get(pk=int(id))
    context = {'setting' : setting, 'logintype': str(request.session['loginType'])}

    return render(request, 'sacco/settings_update.html', context)
    
def update_delete_setting(request):
    if request.method == 'POST':
        id = request.POST.get("setting_id")
        if 'delete_setting' in request.POST:
            Setting.objects.filter(id=id).delete()
        else:
            value = str(request.POST.get("settingValue"))
            Setting.objects.filter(pk=int(id)).update(SettingValue=value)
        return redirect("sacco:my_settings")
