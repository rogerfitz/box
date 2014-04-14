from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import User, Profile
from preferences.forms import PreferencesForm

@login_required
def index(request):
	user = User.objects.get(id=request.user.id)
	profile = user.profile
	preferences = profile.preferences

	form = PreferencesForm(instance=preferences)	
	
	if request.method == 'POST':
		form = PreferencesForm(request.POST, instance=preferences)
		if form.is_valid():	
			print form.data
			user.profile.preferences = form.save()
			user.save()
			return redirect('/home')


	return render(request, 'home/editPreferences.html', {'form': form})
