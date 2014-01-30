from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from boxes.models import Box
from users.forms import UserForm, ProfileForm, FullProfileForm
from users.models import User, Profile
from products.models import Product
from box.settings import boxFeedback

@login_required
def index(request):
	if request.user.is_superuser:
		return redirect('/boxman/')
	user = User.objects.get(id=request.user.id)
	if user.profile is None:
		return addProfile(request)

	if request.method == 'POST':
		try:
			obj, id, feedback = request.POST['data'].split('.')
			if obj == "box":
				pass#Box.
		except:
			pass

		return render(request, 'home/index.html', {'user': user, 'boxFeedback': boxFeedback})
	return render(request, 'home/index.html')

@login_required
def addProfile(request):
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)		
		form = FullProfileForm(request.POST)
		user.profile = form.save()
		user.save()
		return index(request)
	else:
		form = FullProfileForm()

	return render(request, 'home/addProfile.html', {'form': form})

@login_required
def editProfile(request):
	profile = (User.objects.get(id=request.user.id)).profile
	if request.method == 'POST':
		form = FullProfileForm(request.POST, instance=profile)
		if form.is_valid():
			user = User.objects.get(id=request.user.id)		
			form = ProfileForm(request.POST)
			user.profile = form.save()
			user.save()
			return redirect('/home')
	form = FullProfileForm(instance=profile)
	return render(request, 'home/editProfile.html', {'form': form})




