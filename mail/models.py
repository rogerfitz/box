from django.db import models
import smtplib
from custom_settings import *

class Mail(models.Model): #move to seperate app
	to = models.EmailField()
	subject = models.CharField(max_length='150')
	body = models.TextField(max_length='3000')

	date_added = models.DateField(auto_now_add=True)
	date_modified = models.DateField(auto_now=True)

	def send(self):
		server = smtplib.SMTP('smtp-mail.outlook.com', 587)
		server.login(email_username, email_password)
		print 'hi'
