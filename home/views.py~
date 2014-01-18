from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from boxes.models import Box
from users.forms import UserForm, ProfileForm, FullProfileForm
from users.models import User, Profile
from products.models import Product

def index(request):
	if request.user.is_authenticated():
                if request.user.is_superuser:
			return redirect('/boxman/')
		user = User.objects.get(id=request.user.id)
		if user.profile is None:
			return addProfile(request)

		boxes= user.profile.boxes.order_by('price')
		for box in boxes:
			products = box.products.all()
			for product in products:
				print product.name
		bz = []
		for box in boxes:
			b = Box()
			b.product=box.products.all()
			b.id=box.id
			bz.append(b)
		
		return render(request, 'home/index.html', {'boxes': boxes, 'user': user})
	return redirect('/login/')

@login_required
def addProfile(request):
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)		
		form = ProfileForm(request.POST)
		user.profile = form.save()
		user.save()
		return index(request)
	else:
		form = ProfileForm()

	return render(request, 'home/addProfile.html', {'form': form})

@login_required
def editProfile(request):
	profile = (User.objects.get(id=request.user.id)).profile
	if request.method == 'POST':
		form = FullProfileForm(request.POST, instance=profile)
		form.save()
		return redirect('/')
	form = FullProfileForm(instance=profile)
	return render(request, 'home/editProfile.html', {'form': form})




