from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.http import HttpResponse
from . models import *
from . forms import OrderForm, CreationUserForm, CastomersForm
from .filters import orderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

@unauthenticated_user
def register(request):
    # form = UserCreationForm()
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    form = CreationUserForm()
    if request.method=='POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # this part is added on signals.py file
            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            # customer.objects.create(
            #     user= user,
            # )

            messages.success(request,"Account Created for "+username)
            return redirect('login')
    context= {'form':form}
    return render(request,'accounts/register.html',context)


@unauthenticated_user
def logedin(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password= password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'username OR password is incorrect...!')

    context = {}
    return render(request,'accounts/login.html',context)


def logedout(request):
    logout(request)
    print('logout',request)
    return redirect('/login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def settings(request):
    User = request.user.customer
    print("user",User)
    # customer = customer.objects.get(name=User.name)
    form = CastomersForm(instance=User)
    if request.method=='POST':
        form = CastomersForm(request.POST, request.FILES, instance=User)
        if form.is_valid():
            form.save()
    
    context = {'form':form,'customer':customer}
    return render(request,'accounts/setting.html',context)



# @admin_only
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user(request):
    order = request.user.customer.order_set.all()
    total_orders = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    # print("ORDER",order)

    context={'order':order,'pending': pending, 'delivered': delivered, 'total_orders': total_orders}
    return render(request,'accounts/user.html',context)



@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    customers = customer.objects.all()
    order = Order.objects.all()

    total_customer = customers.count()
    total_orders = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    context = {'customer': customers, 'order': order, 'total_customer': total_customer,
               'pending': pending, 'delivered': delivered, 'total_orders': total_orders}

    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    product = Product.objects.all()
    return render(request, 'accounts/product.html', {'product': product})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, customer_id):
    customerss = customer.objects.get(id=customer_id)
    orders = customerss.order_set.all()
    total_order = customerss.order_set.all().count()

    myFilter = orderFilter(request.GET,queryset=orders)
    orders = myFilter.qs

    context = {'customer': customerss,
               'orders': orders, 'total_order': total_order,'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        customer, Order, fields=('product', 'status'), extra=10)
    # extra =10 makes 10 times fileds for ordering
    Customers = customer.objects.get(id=pk)
    # formset = OrderFormSet(queryset=Order.objects.none(), instance=Customers)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=Customers)
    # form = OrderForm(initial={'customer':Customers})   #for one order
    # if request.method=='POST':
    #     # print('printing',request.POST)
    #     form = OrderForm(request.POST)
    #     if form.is_valid:
    #         form.save()
    #         return redirect('/')
    # context = {'form':form}

    if request.method == 'POST':
        # print('printing',request.POST)

        formset = OrderFormSet(request.POST, instance=Customers)
        if formset.is_valid:
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=[])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    print('ORDER:', form)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'forms': form}
    return render(request, 'accounts/order_form.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def deleteOrder(request, pk_del):
    order = Order.objects.get(id=pk_del)
    # print('obejcts',order)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)
