from django.shortcuts import render
from .models import ngoModel,volunteerModel,loginModel
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def ngoForm(request):
    if request.method=='POST':
        name=request.POST.get("name")
        ngoid=request.POST.get("id")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        alt_phone=request.POST.get("altphone")
        street1=request.POST.get("street1")
        street2=request.POST.get("street2")
        country=request.POST.get("Country")
        city=request.POST.get("City")
        region=request.POST.get("Region")
        postalcode=request.POST.get("Postalcode")
        domain=request.POST.get("domain")
        savedata=ngoModel(ngo_name=name,ngo_reg_id=ngoid,ngo_email=email,phone_no=phone,alt_phone_no=alt_phone,address_street1=street1,address_street2=street2,Country=country,City=city,Region=region,Postal_code=postalcode,ngo_domain=domain)
        savedata.save()
    return render(request,"ngo_reg.html")



@csrf_exempt
def volunteerForm(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        dob=request.POST.get("dob")
        gender=request.POST.get("gender")
        address1=request.POST.get("address1")
        address2=request.POST.get("address2")
        country=request.POST.get("Country")
        city=request.POST.get("City")
        region=request.POST.get("Region")
        postalcode=request.POST.get("Postalcode")
        Qualification=request.POST.get("Qualification")
        Domain=request.POST.get("Domain")
        savedata=volunteerModel(volunteer_name=name,volunteer_email=email,phonenumber=phone,dob=dob,gender=gender,address1=address1,address2=address2,Country=country,city=city,region=region,postalcode=postalcode,education=Qualification,volunteer_domain=Domain)
        savedata.save()
    return render(request,"volunteer_reg.html")

@csrf_exempt
def loginForm(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        savedata=loginModel(user_name=username,password=password)
        savedata.save()
    return render(request,"login.html")



@csrf_exempt
def Random(request):
    if request.method=='POST':
        password=request.POST.get("password")
        savedata=loginModel(password=password)
        savedata.save()
    return render(request,"login.html")