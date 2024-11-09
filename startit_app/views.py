from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Items
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

def home_page(request):
    categories = Category.objects.all()
    items = Items.objects.all().order_by('-data')  # Ensure 'data' is the correct field

    context = {
        'categories': categories,
        'items': items
    }
    return render(request, "home.html", context)  # Adjusted path

def items_page(request):
    items = Items.objects.all().order_by('-data')  # Ensure 'data' is the correct field
    context = {
        'items': items  # Renamed for clarity
    } 
    return render(request, "items.html", context)  # Adjusted path

def categories_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    } 
    return render(request, "categories.html", context)  # Adjusted path

def item_elem_page(request, pk):
    item = get_object_or_404(Items, pk=pk)
    context = {
        'item': item
    }
    return render(request, "item-elem.html", context)  # Adjusted path

def items_by_category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    items = Items.objects.filter(category=category)
    context = {
        'category': category,
        'items': items
    }
    return render(request, 'items-by-category.html', context)  # Adjusted path


def sign_up_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, "./sign-up.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, "./login.html", context)

def logout_action(request):
    logout(request)
    return redirect('home')