from django.shortcuts import render
from django.http import HttpResponse
#Create your views here
from .models import *



# Create your views here.
#What the user views (this connects the admin page to the html pages)
def home (request):
    return render(request, "accounts/index.html")

def dashboard (request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    #TOTAL
    t_customers = customers.count()
    t_orders = orders.count()

    #Order Information
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    #Dict.
    information = {"orders":orders ,"customers":customers, "t_orders":t_orders, "delivered":delivered, "pending":pending}

    return render(request, "accounts/dashboard.html",information)

def products (request):
    products = Product.objects.all()
    return render(request, "accounts/products.html",{"products":products})

def customers (request):
    return render(request, "accounts/customers.html")



#Register
# def registerPage(request):
#     information = {}
#     return render(request,"accounts/register.html", information)

# def loginPage(request):
#     information = {}
#     return render(request, "accounts/register.html", information)

#Forms
#Create Order
def createOrder(request):
    information = {}
    return render(request, "accounts/order_form.html", information)