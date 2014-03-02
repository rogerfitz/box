from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from boxes.models import Box, BoxFeedback
from users.forms import UserForm, ProfileForm, FullProfileForm, AccessForm
from users.models import User, Profile
from products.models import Product, ProductFeedback
from box.settings import boxFeedback, prodFeedback
from django.core.mail import send_mail
#import logging

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
			obj = Box.objects.get(id=id)
			feedbackObj = BoxFeedback()
		elif obj == 'product':
			obj = Product.objects.get(id=id)
			feedbackObj = ProductFeedback()

		for junk in obj.feedback.filter(user=user):
			junk.delete()
		

		feedbackObj.feedback = str(feedback)
		feedbackObj.save()
		
		feedbackObj.user.add(user)
		feedbackObj.save()
		obj.feedback.add(feedbackObj)

		obj.save()	
			
		return render(request, 'home/index.html', {'user': user, 'boxFeedback': boxFeedback, 'prodFeedback': prodFeedback})
	  except:
		try:
			profile = (User.objects.get(id=request.user.id)).profile
			form = AccessForm(request.POST, instance=profile)
			if request.method == 'POST':
				if form.is_valid():
					user = User.objects.get(id=request.user.id)		
					user.profile = form.save()
					user.save()
					return redirect('/home')
			
		except:
			pass
	form = AccessForm(request.POST)
	return render(request, 'home/index.html', {'user': user, 'boxFeedback': boxFeedback, 'prodFeedback': prodFeedback, 'access_form': form})

@login_required
def addProfile(request):
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)		
		form = FullProfileForm(request.POST)
		user.profile = form.save()
		user.save()
		send_mail('Nice Package', 'Hi '+str(user.profile)+',\n\nThanks for creating an account.\nThe Nice Package Team -- www.thenicepackage.com\n\nFor any questions or if you are wondering just how our packages become so nice, feel free to contact Matteo matteo@thenicepackage.com', 'matteo@thenicepackage.com', [str(user.username)], fail_silently=True)	
		return redirect('/home/preferences')

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
			user.profile = form.save()
			user.save()
			return redirect('/home')
	form = FullProfileForm(instance=profile)
	return render(request, 'home/editProfile.html', {'form': form})

def ipn(request):
	get = request.GET
	post = request.POST
	f = open('/home/ubuntu/projects/box/ipn.log', 'w')
	f.write('test')
	#f.write(get)
	#f.write(post)
	f.close()
	return render(request, 'debug.html', {'get': get, 'post': post})


