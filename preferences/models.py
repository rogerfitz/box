from django.db import models

class Preferences(models.Model):
	shirt_size = models.CharField(max_length=5, null=True, choices=(('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')))
	underwear_type = models.CharField(max_length=5, null=True, choices=(('BX', 'Boxers'), ('BRF', 'Briefs'), ('BXBRF', 'Boxer Briefs')))
	underwear_size = models.CharField(max_length=5, null=True, choices=(('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')))
	hobby1 = models.CharField(max_length=20, null=True, default='') #Generic choice handling?
	hobby2 = models.CharField(max_length=20, null=True, default='')
	hobby3 = models.CharField(max_length=20, null=True, default='')
	alcohol = models.CharField(max_length=3, null=True, choices=(('G', 'Gin'), ('W', 'Whiskey'), ('R', 'Rum'), ('V', 'Vodka'), ('T', 'Tequila')))
	hometown = models.CharField(max_length=30, null=True )
	fraternity = models.BooleanField(default=1, choices=((0, 'Yes'), (1, 'No')))
	party = models.BooleanField(default=1 , choices=((0, 'Yes'), (1, 'No')))

	#allow user to suggest their own preference (json?)
