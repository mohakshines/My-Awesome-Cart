from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order
from math import ceil

def index(request):
        products = Product.objects.all()
        # n = len(products)
        # nSlides = (n//4) + ceil((n/4)-(n//4))
        # params={'product': products,'range': range(1,nSlides),'no_of_slides': nSlides}
        # allProds=[[products,range(1,nSlides),nSlides],
        #        [products,range(1,nSlides),nSlides]]
        allProds=[]
        catprods=Product.objects.values('category','id')
        cats={item['category'] for item in catprods}
        for i in cats:
            prod=Product.objects.filter(category=i)
            n = len(prod)
            nSlides = (n // 4) + ceil((n / 4) - (n // 4))
            allProds.append([prod,range(1,nSlides),nSlides])
        params={'allProds':allProds}
        return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()


    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def checkout(request):
    if request.method=='POST':
        items_json=request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address1','')+" " + request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        order = Order(items_json=items_json,name=name,email=email,phone=phone,address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        thank = True
        id = order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,'shop/checkout.html')

def productview(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request,'shop/prodview.html',{'product':product[0]})