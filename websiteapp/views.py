from django.shortcuts import render, redirect
from backendapp.models import addcategorydb, producpagedb, admincontactdb
from websiteapp.models import customrregisterdb

# Create your views here.
def Homepage(request):
    data = addcategorydb.objects.all()
    return render(request, "home.html", {'data':data})
def aboutpage(request):
    return render(request, "about.html")
def contactpage(request):
    return render(request, "contact.html")
def blogpage(request):
    return render(request, "blog.html")

def discategory(request,itemCatg):
    data = addcategorydb.objects.all()
    print("===itemCatg===", itemCatg)
    catg=itemCatg.upper()
    products =producpagedb.objects.filter(Category=itemCatg)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request,"display_catgry.html",context)
def prodcsingle(request,dataid):
    data = addcategorydb.objects.all()
    dat = producpagedb.objects.get(id=dataid)
    return render(request, "product_single.html", {'data':data,'dat':dat})

def loginregister(request):
    return render(request, "login_or_register.html")

def saveregister(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        pasw = request.POST.get('password')
        cpasw = request.POST.get('cpassword')
        obj = customrregisterdb(Name=name, Email=email, Password=pasw, Confirmpassword=cpasw)
        obj.save()
        return redirect(loginregister)






def savecontactadmin(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        ema = request.POST.get('email')
        sub = request.POST.get('subject')
        mes = request.POST.get('message')
        obj = admincontactdb(Name=nam, Email=ema, Subject=sub, Message=mes)
        obj.save()
        return redirect(contactpage)
