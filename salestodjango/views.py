from django.shortcuts import render
import json
from salestodjango.models import SfUsers,Account,Contact
from salestodjango import gettoken,accessdata
def index(request):
    context={}
    context["header"]="Assignment To fetch Data from salesforce and store it to local database"
    SfUsers.objects.all().delete()
    Account.objects.all().delete()
    Contact.objects.all().delete()
    at=gettoken.get_token()
    context["token"]=at[0]
    userdata=accessdata.Insertusers()
    for data in userdata["records"]:
        tab=SfUsers.objects.create(Username=data["Username"],FirstName=data["FirstName"],LastName=data["LastName"],Email=data["Email"])
    accountdata=accessdata.InsertAccount()
    for data1 in accountdata["records"]:
        tab=Account.objects.create(Name=data1["Name"],AccountNumber=data1["AccountNumber"],AnnualRevenue=data1["AnnualRevenue"],LastActivityDate=data1["LastActivityDate"])
    context["data1"]=Account.objects.all()[:5]
    contactdata=accessdata.InsertContact()
    for data2 in contactdata["records"]:
        tab=Contact.objects.create(Name=data2["Name"],Email=data2["Email"],AccountID=data2["AccountId"],Phone=data2["Phone"])
    context["data1"]=Account.objects.exclude(AnnualRevenue__isnull=True)[:5]
    context["data2"]=Contact.objects.all()[:5]
    context["data"]=SfUsers.objects.all()
    return render(request,"index.html",context)

