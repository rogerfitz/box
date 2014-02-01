from django.shortcuts import render, redirect
from users.models import User, Profile
from users.forms import UserForm
from boxes.models import Box
from products.models import Product
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import logout_then_login
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

@user_passes_test(lambda u: u.is_superuser, login_url='/login')
def index(request):
	#sort by state
	users = User.objects.exclude(is_superuser=True).exclude(profile_id__isnull=True)
	for u in users:
		print u.username
	if request.method == 'POST':
		action, prof_id = request.POST['data'].split('.')
		prof = Profile.objects.get(id=prof_id)
		print action
		if action == 'shipped':
			prof.ship()
		elif action == 'customBox':
			return HttpResponse('boxman/users/assignBox/'+str(prof_id)+'/', content_type="text/plain")
		elif action == 'paid':
			prof.pay()
		elif action == 'delete':
			return deleteUser(request, prof.user.id)
		else:
			print action+' error!!!!'
		return redirect('boxman/users')
	return render(request, 'admin/users/list.html', {'users': users})

@user_passes_test(lambda u: u.is_superuser, login_url='/login')
def addUser(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		form = form.save(commit=False)
		form.save()
		return redirect('/users/')
	else:
		form = UserForm()

	return render(request, 'admin/users/add.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser, login_url='/login')
def deleteUser(request, user_id):
	(User.objects.get(id=user_id).profile).delete()
	#User.objects.get(id=user_id).delete()
	return redirect('/boxman/users/')

@user_passes_test(lambda u: u.is_superuser, login_url='/login')
def assignBox(request, prof_id):
	products= Product.objects.all()
	if request.method == 'POST':
		prof = Profile.objects.get(id=prof_id)
		box=Box()
		products = []
		box.price = 0.0
		for product_id in request.POST.getlist('id'):
			p = Product.objects.get(id=int(product_id))
			box.price += float(p.price_per_box)
			products.append(p)
		box.save()

		for p in products:
			p.item_count-=p.items_in_box
			p.save()
			box.products.add(p)

		prof.box_to_ship = box
		prof.save()
		
		return redirect('/boxman/users/')
	return render(request, 'admin/boxes/products.html', {'products': products})

def logout(request):
	return logout_then_login(request, '/')

def register(request):
    if request.method == 'POST':
	form = UserForm(request.POST)
        if form.is_valid():
		user = form.save()
		user =  authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
		login(request, user)		
            	return redirect('/home')
    else:
        form = UserForm()
    return render(request, "users/register.html", {
        'form': form,
    })

@user_passes_test(lambda u: u.is_superuser, login_url='/login')
def profile(request):
	users = User.objects.order_by('username')
	return render(request, 'users/list.html', {'users': users})
