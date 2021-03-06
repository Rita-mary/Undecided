from django.shortcuts import redirect, render
from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.all()
    context ={
        'products' : products
    }
    return render(request , 'app1/index.html', context)
def product_details(request , id):
    product = Product.objects.get(id = id)
    context = {
        'product' : product
    }
    return render(request , 'app1/product_details.html', context)

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES['upload']
        product = Product(name = name, price = price, description = description, image = image) 
        product.save()
        return redirect('/app1/index')
    return render(request , 'app1/add_products.html')