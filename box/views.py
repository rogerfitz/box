from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

def index(request):
	if request.user.is_superuser:
		return render(request, 'admin/index.html')
	return render(request, 'index.html')