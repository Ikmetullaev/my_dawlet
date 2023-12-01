from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse        
from .models import Post, Dawlet
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from myblog.forms import UserRegistrationForm, DawletForm, DawletchangeForm
from myblog.models import Dawlet, Category
@staff_member_required()
def dawlet_list(request):
    product = Dawlet.objects.all()
    return render(request=request, template_name='myblog/tovar_list.html', context={'product': product})

def dawlet_update(request, product_id):
    product = Dawlet.objects.get(id=product_id)
    if request.method == 'POST':
        form = DawletchangeForm(data = request.POST, instance = product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myblog:dawlets'))
    else:
        form = DawletchangeForm(instance=Dawlet.objects.get(id=product_id))
    # context = {'form': form}
    return render(request,'myblog/dawlet.html', {'form':form, 'product':product})

@staff_member_required()
def dawlet_add(request):
    if request.method == 'POST':
        form = DawletForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myblog:dawlet_add'))
    else:
        form = DawletForm()
    context = {'form': form}
    return render(request,'myblog/dawlet.html', context)

def servicespage(request):  
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'myblog/services.html', context)
def servicesDetail(request, pk):
    posts = Post.objects.get(id=pk)
    context = {
        'posts': posts
    }
    return render(request, 'myblog/about_detail.html', context)
def homepage(request):
    return render(request,'myblog/home.html')
def aboutpage(request):
    return render(request, 'myblog/about.html')
def loginpage(request):     
    return render(request, 'myblog/login.html')
def loginspage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'myblog/logins.html', {'form': form})
def registration(request):
    if request.method == 'POST':

        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
        
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, template_name='myblog/register.html', context=context)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
def menu(request, slug=None, page=1):
    if slug: 
        category = Category.objects.get(slug=slug)
        product = Dawlet.objects.filter(cat=category)
    else:
        product = Dawlet.objects.all()
    context = {'category': Category.objects.all(), 'product': product}
    return render(request, 'myblog/menu.html', context=context)
