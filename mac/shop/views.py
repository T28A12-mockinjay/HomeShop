from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdates
from math import ceil
import json
# Create your views here.

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')
        contact = Contact(name=name, email=email, phone=phone, query=query)
        contact.save()
        thank = True
        return render(request, 'shop/contact.html', {'thank': thank})


    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get("orderId", '')
        email = request.POST.get('email', '')
        print(f"{orderId} and {email}")
        try:
            order = Orders.objects.filter(order_id=orderId,email=email)    #here 'order' is a list
            print(order)
            if len(order)>0:
                update = OrderUpdates.objects.filter(order_id=orderId)
                print(update)
                updates=[]
                for k in update:
                    updates.append({'text':k.update_desc,'time':k.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)      #string is passed in form of f-string in HttpResponse
            else:
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse("{}")
    return render(request, 'shop/tracker.html')

def search(request):
    return HttpResponse("We are in search")

def prodview(request, myid):
    prod = Product.objects.filter(id=myid)
    print(prod[0])
    return render(request, 'shop/prodview.html', {'prod': prod[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get("itemsJson", '')
        print(items_json)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        add = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json,name=name,email=email,add=add,city=city,state=state,
                       zip_code=zip_code,phone=phone)
        order.save()
        thank = True
        id = order.order_id
        update = OrderUpdates(order_id=id,update_desc="The order has been placed")
        update.save()
        return render(request, 'shop/checkout.html',{'thank': thank,'id': id})
    return render(request, 'shop/checkout.html')

