from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from  .models import *
# Create your views here.

def main(request):
    brand  = Brand.objects.all()
    sneakercard  = SneakerCard.objects.all()
    return render(request, 'index.html', {'sneakercard': sneakercard, 'brand': brand})

def base(request):
    return render(request, 'base.html')

def more(request, id):
    more = SneakerCard.objects.get(id = id)
    return render(request, 'more.html',{'more': more} )

res = {}
def addcard(request, pk):
    cart_session = request.session.get('cart_session', [])
    print(cart_session)
    cart_session.append(pk)
    request.session['cart_session'] = cart_session
    products_card = SneakerCard.objects.filter(id__in=cart_session)
    for i in products_card:
        count = cart_session.count(i.id)
        if count == 1:
           return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/card')

def card(request):
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    products_card = SneakerCard.objects.filter(id__in=cart_session)
    all_products_sum = 0
    for i in products_card:
        count = cart_session.count(i.id)
        sum = count * i.price
        all_products_sum = all_products_sum + sum

    return render(request, 'card.html',
    {'products_card': products_card ,
     'count_of_product':count_of_product, 
     'all_products_sum':all_products_sum })



def removecard(request, pk):
    cart_session = request.session.get('cart_session', [])
    carts = []
    for id in cart_session:
        if id != pk:
            carts.append(id)
    request.session['cart_session'] = carts
    return HttpResponseRedirect('/card')


    