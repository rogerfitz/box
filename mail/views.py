from django.shortcuts import render, redirect
from django.core.mail import send_mail

def index(request):
	#
	return render(request, 'users/list.html')
