from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import User, Profile
from preferences.forms import PreferencesForm

@login_required
def index(request):
	profile = (User.objects.get(id=request.user.id)).profile
	preferences = profile.preferences

	if request.method == 'POST':
		form = PreferencesForm(request.POST, instance=preferences)
		if form.is_valid():	
			form = PreferencesForm(request.POST)
			
			profile.preferences = form.save()
			profile.save()
			return redirect('/home')
	form = PreferencesForm(instance=preferences)

	return render(request, 'home/editPreferences.html', {'form': form})
