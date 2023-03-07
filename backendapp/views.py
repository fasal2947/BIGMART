from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from backendapp.models import addadmindb, addcategorydb, producpagedb, admincontactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def indexpage(req):
    return render(req, "index.html")
def addadminpage(request):
    return render(request, "addadmin.html")
def saveaddadmin(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mb = request.POST.get('mobile')
        un = request.POST.get('user')
        ps = request.POST.get('password')
        im = request.FILES['image']
        obj = addadmindb(Name=na, Email=em, Mobile=mb, User=un, Password=ps, Image=im)
        obj.save()
        return redirect(addadminpage)
def Displayaddadmin(request):
    data = addadmindb.objects.all()
    return render(request, "DisplayAddAdmin.html", {'data':data})
def Editaddadmin(request, dataid):
    data = addadmindb.objects.get(id=dataid)
    print(data)
    return render(request, "EditAddAdminpage.html", {'data': data})
def Updateaddadmindata(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mb = request.POST.get('mobile')
        un = request.POST.get('user')
        ps = request.POST.get('password')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = addadmindb.objects.get(id=dataid).Image
        addadmindb.objects.filter(id=dataid).update(Name=na, Email=em, Mobile=mb, User=un, Password=ps, Image=file)
        return redirect(Displayaddadmin)

def deleteaddadmindata(request, dataid):
    data = addadmindb.objects.filter(id=dataid)
    data.delete()
    return redirect(Displayaddadmin)

def addcategorypage(request):
    return render(request, "category.html")

def savecategorypage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ds = request.POST.get('description')
        im = request.FILES['image']
        obj = addcategorydb(Name=na, Description=ds, Image=im)
        obj.save()
        return redirect(addcategorypage)

def displaycategory(request):
    data = addcategorydb.objects.all()
    return render(request, "Displaycategory.html", {'data':data})

def Editcategorypage(request, dataid):
    data = addcategorydb.objects.get(id=dataid)
    print(data)
    return render(request, "Editcategorypage.html", {'data':data})
def Updatecategorypage(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        ds = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = addcategorydb.objects.get(id=dataid).Image
        addcategorydb.objects.filter(id=dataid).update(Name=na, Description=ds, Image=file)
        return redirect(displaycategory)

def Deletecategory(request, dataid):
    data = addcategorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)
def productpage(request):
    data = addcategorydb.objects.all()
    return render(request, "products.html", {'data':data})
def productsavepage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pr = request.POST.get('prize')
        qn = request.POST.get('quantity')
        ca = request.POST.get('category')
        ds = request.POST.get('description')
        im = request.FILES['image']
        obj = producpagedb(Name=na, Prize=pr, Quantity=qn, Category=ca, Description=ds, Image=im)
        obj.save()
        return redirect(productpage)

def DisplayProduct(request):
    data = producpagedb.objects.all()
    return render(request, "Displayproductpage.html", {'data':data})
def editproductpage(request, dataid):
    data = producpagedb.objects.get(id=dataid)
    print(data)
    da = addcategorydb.objects.all()
    return render(request, "Editproductpage.html", {'datas':data, 'da':da})
def updateproductdata(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        pr = request.POST.get('prize')
        qn = request.POST.get('quantity')
        ca = request.POST.get('category')
        ds = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = producpagedb.objects.get(id=dataid).Image
        producpagedb.objects.filter(id=dataid).update(Name=na, Prize=pr, Quantity=qn, Category=ca, Description=ds, Image=file)
        return redirect(DisplayProduct)
def Deleteproduct(request, dataid):
    data = producpagedb.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayProduct)

def loginpage(request):
    return render(request, "loginpage.html")

def adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('pass')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username']=username_r
                request.session['pass']=password_r
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def logout(request):
    del request.session['username']
    del request.session['pass']
    return redirect(loginpage)

def displaycontc(request,):
    data = admincontactdb.objects.all()
    return render(request, "dispalycontact.html", {'data': data})

def displaycontctdelete(request, dataid):
    data = admincontactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontc)













