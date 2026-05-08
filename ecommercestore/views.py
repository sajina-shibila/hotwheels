from django.shortcuts import render,redirect
def index(request):
    return render(request,"index.html")

from.models import User
from django.contrib import messages
def register(request):
    if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       password = request.POST.get('password')
       address = request.POST.get('location')
       phone = request.POST.get('phone')
       if User.objects.filter(email=email).exists():
          messages.error(request, 'Email already registered.')
       else:
          User.objects.create(name=name, email=email, password=password, address=address, phone=phone)
          messages.success (request, 'Registration successful!')
          return redirect('index')
    return render (request, 'register.html')


def login(request):
   if request.method == 'POST':
         email = request.POST.get('email')
         password = request.POST.get('password')
         try:
            user = User.objects.get(email=email, password=password)
            request.session['email'] = user.email
            return redirect('index')
         except User. DoesNotExist:
            return render (request, 'login.html', {'error': 'Invalid email or password.'})
   return render (request, 'login.html')


def profile(request):
   email = request.session.get('email')

   if email is not None:
          try:
              user = User.objects.get(email=email)
              return render (request, 'profile.html', {'user': user})
          except User. DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('login')
   else:
          messages.warning (request, "You need to log in to access your profile.")
          return redirect('login')
   
def logout(request):
    request.session.flush()
    return redirect('index')

def editprofile(request):
    email = request.session.get('email') 
    user = User.objects.get(email=email)  # Get the User object
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        user.name = name
        user.phone = phone
        user.address = location
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')  
    return render(request, 'profile.html', {'user': user})

def userlist(request):
    user=User.objects.all()
    return render(request,'userlist.html',{'user':user})
def deleteuser(request,id):
    data=User.objects.filter(id=id)
    data.delete()
    return redirect('userlist')


from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        from django.shortcuts import render, redirect
from .models import Product

# Add Product View (NO forms.py)
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        # Save data manually
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            category=category,
            image=image
        )

        return redirect('product_list')

    return render(request, 'add_product.html')


# Product List View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Cart, Product,User


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    email = request.session.get('email')

    if email:
        user = get_object_or_404(User, email=email)

        cart_item, created = Cart.objects.get_or_create(
            user=user,
            product=product,
            defaults={'quantity': 1}
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('cart')
    else:
        return JsonResponse({'error': 'Login first'}, status=400)
    
def cart(request):
    email = request.session.get('email')

    if email:
        user = get_object_or_404(User, email=email)
        cart_items = Cart.objects.filter(user=user)

        for item in cart_items:
            item.total_price = item.product.price * item.quantity

        total_price = sum(item.total_price for item in cart_items)

        return render(request, 'cart.html', {
            'cart_items': cart_items,
            'total_price': total_price
        })
    else:
        return render(request, 'cart.html', {
            'error': 'Login required'
        })
    
def delete_cart(request, id):
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, id=id)
        cart_item.delete()
        return redirect('cart')

    return redirect('cart')


