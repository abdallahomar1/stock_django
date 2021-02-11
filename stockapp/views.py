from django.shortcuts import render, redirect
from django.urls import reverse
from stockapp.models import prodect
from . models import orders5 , prodect
from . filters import ordersFilter
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import new_order

# Create your views here.
def all_orders(request):
    orders = orders5.objects.all()
    paginator = Paginator(orders, 30)
    my_filter = ordersFilter(request.GET,queryset=orders)
    orders = my_filter.qs
    
    return render(request, '3.html', {'order':orders, 'filter':my_filter})
def karton_datail(request, id):
    kar = orders5.objects.get(id=id)
    return render(request, '2.html', {'karton':kar})

def ff(request):
    pp = prodect.objects.filter(cwan__lte=30)
   
    return render(request, '4.html', {'prodect':pp})

def prodect_datial(request, id):
    prodect3 = orders5.objects.get(id=id)
    return render(request, '5.html', {'prodect':prodect3})

def fatora(request, id):
    fatoras = orders5.objects.get(id=id)
    if request.method == 'POST' :
        form = new_order(request.post)
        if form.is_valid() :
            form.save()
            return redirect(reverse('home:fatora'))
    else :
        form = new_order()
    return render(request, 'fatora.html', {'karton':form})