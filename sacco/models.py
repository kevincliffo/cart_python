from django.db import models
from datetime import datetime
from django.utils import timezone

class Member(models.Model):
    MemberNo = models.CharField(max_length=100, default="")
    FirstName = models.CharField(max_length=100, default="")
    LastName = models.CharField(max_length=100, default="")
    MobileNo = models.CharField(max_length=100, default="")
    IdNumber = models.CharField(max_length=100, default="")
    Email = models.CharField(max_length=100, default="")

    class Type(models.TextChoices):
        Member = '1', "Member"
        Chairperson = '2', "Chairperson"
        ViceChairperson = '3', "Vice Chairperson"
        Treasurer = '4', "Treasurer"
        AssistantTreasurer = '5', "Assistant Treasurer"
        Secretary = '6', "Secretary"
        AssistantSecretary = '7', "Assistant Secretary"
        OrganizingSecretary = '8', "Organizing Secretary"
        TimeKeeper = '9', "Time Keeper"
    MemberType = models.CharField(max_length=20, choices=Type.choices, default=Type.Member)

    class GenderType(models.TextChoices):
        Male = '1', "Male"
        Female = '2', "Female"
    MemberGender = models.CharField(max_length=20, choices=GenderType.choices, default=GenderType.Male)

    Password = models.CharField(max_length=100, default="")
    NextOfKinFullName = models.CharField(max_length=100, default="")
    NextOfKinMobileNo = models.CharField(max_length=100, default="")
    NextOfKinRelationship = models.CharField(max_length=100, default="")
    LastLogin = models.DateTimeField(default=datetime.utcnow().replace(tzinfo=timezone.utc))
    CreatedDate = models.DateTimeField(default=datetime.utcnow().replace(tzinfo=timezone.utc))
    
    def __str__(self):
        return self.name

class Financial(models.Model):
    MemberNo = models.ForeignKey(Member, on_delete=models.CASCADE, default='')
    FullName = models.CharField(max_length=100, default="")
    MobileNo = models.CharField(max_length=100, default="")
    IdNumber = models.CharField(max_length=100, default="")
    Salary = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    Deduction = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    Contribution = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    PendingLoans = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    
    def __str__(self):
        return self.name    

class Setting(models.Model):
    SettingKey = models.CharField(max_length=100, default="")
    SettingName = models.CharField(max_length=100, default="")
    SettingValue = models.CharField(max_length=255, default="")
    
    def __str__(self):
        return self.name    

class Ticket(models.Model):
    Title = models.CharField(max_length=100, default="")
    Sender = models.CharField(max_length=100, default="")
    Content = models.CharField(max_length=255, default="")
    TicketRead = models.BooleanField(default=False) 
    CreatedDate = models.DateTimeField()
    ReadDate = models.DateTimeField()
    
    def __str__(self):
        return self.name    

class User(models.Model):
    FirstName = models.CharField(max_length=100, default="")
    LastName = models.CharField(max_length=100, default="")
    Email = models.CharField(max_length=100, default="")
    Password = models.CharField(max_length=100, default="")
    IdNumber = models.CharField(max_length=100, default="")
    MobileNo = models.CharField(max_length=100, default="")
    LastLogin = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    
    def __str__(self):
        return self.name