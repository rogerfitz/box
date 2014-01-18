from django.shortcuts import render, redirect
from users.models import User, Profile
from users.forms import UserForm
from boxes.models import Box
from products.models import Product
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import logout_then_login
from django.contrib.auth import authenticate, login

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
	#sort by state
	users = User.objects.exclude(is_superuser=True)
	return render(request, 'admin/users/list.html', {'users': users})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def addUser(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		form = form.save(commit=False)
		print form.data
		form.save()
		return redirect('/users/')
	else:
		form = UserForm()

	return render(request, 'admin/users/add.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def deleteUser(request, user_id):
	User.objects.get(id=user_id).delete()
	return redirect('/boxman/users/')

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def assignBox(request, prof_id):
	products= Product.objects.all()
	if request.method == 'POST':
		prof = Profile.objects.get(id=prof_id)
		box=Box()
		products = []
		box.price = 0.0
		for product_id in request.POST.getlist('id'):
			p = Product.objects.get(id=int(product_id))
			box.price += float(p.price)
			products.append(p)
		box.save()

		for p in products:
			box.products.add(p)

		prof.box_to_ship = box
		print prof.box_to_ship
		prof.save()
		
		return redirect('/boxman/users/')
	return render(request, 'admin/boxes/products.html', {'products': products})

def logout(request):
	return logout_then_login(request, '/')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
		form = UserForm(request.POST)
		user = form.save()
		user =  authenticate(username=request.POST['username'], password=request.POST['password1'])
		login(request, user)		
            	return redirect('/')
    else:
        form = UserForm()
    return render(request, "users/register.html", {
        'form': form,
    })

def profile(request):
	users = User.objects.order_by('username')
	return render(request, 'users/list.html', {'users': users})
