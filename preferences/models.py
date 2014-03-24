from django.db import models

class Preferences(models.Model):
	shirt_size = models.CharField(max_length=5, blank=True, choices=(('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')))
	underwear_type = models.CharField(max_length=5, blank=True, choices=(('BX', 'Boxers'), ('BRF', 'Briefs'), ('BXBRF', 'Boxer Briefs')))
	underwear_size = models.CharField(max_length=5, blank=True, choices=(('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')))
	hobby1 = models.CharField(max_length=20, blank=True, default='') #Generic choice handling?
	hobby2 = models.CharField(help_text="optional", max_length=20, blank=True, default='')
	hobby3 = models.CharField(help_text="optional", max_length=20, blank=True, default='')
	alcohol = models.CharField(verbose_name="Favorite Alcohol", max_length=3, blank=True, help_text="We might send you some non-alcoholic beverages or creative products that pair well with a certain alcohol", choices=(('G', 'Gin'), ('W', 'Whiskey'), ('R', 'Rum'), ('V', 'Vodka'), ('T', 'Tequila'),('N', "Don't Drink"),))
	#hometown = models.CharField(max_length=30, blank=True )
	adj1 = models.CharField(verbose_name='Adjective to describe you?' , max_length=20, blank=True, default='')
	adj2 = models.CharField(help_text="optional", verbose_name='Second adjective to describe you?' , max_length=20, blank=True, default='')
	adj3 = models.CharField(help_text="optional", verbose_name='Third adjective to describe you?' , max_length=20, blank=True, default='')
	fraternity = models.BooleanField(verbose_name="Are you in a fraternity?", default=1, choices=((1, 'Yes'), (0, 'No')))
	party = models.BooleanField(verbose_name="Do you like to party?", default=1 , choices=((1, 'Yes'), (0, 'No')))
	novelty = models.BooleanField(verbose_name="Do you like funny gifts?", default=0, choices=((1, 'Yes'), (0, 'No')))
	clip_on = models.BooleanField(verbose_name="Does a clip-on bowtie upset you?", default=1, choices=((1, 'Yes'), (0, 'No')))

	#allow user to suggest their own preference (json?)
