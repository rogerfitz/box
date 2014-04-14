from django.db import models

yes_no = ((True, 'Yes'), (False, 'No'))

class Preferences(models.Model):
	shirt_size = models.CharField(max_length=5, blank=True, choices=(('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')))
	underwear_type = models.CharField(max_length=5, blank=True, choices=(('BX', 'Boxers'), ('BRF', 'Briefs'), ('BXBRF', 'Boxer Briefs')))
	underwear_size = models.CharField(max_length=5, blank=True, choices=(('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')))
	hobby1 = models.CharField(max_length=20, blank=True, default='') #Generic choice handling?
	hobby2 = models.CharField(help_text="optional", max_length=20, blank=True, default='')
	hobby3 = models.CharField(help_text="optional", max_length=20, blank=True, default='')

	alcohol = models.CharField(verbose_name="Favorite Alcohol", max_length=3, blank=True, help_text="We might send you some non-alcoholic beverages or creative products that pair well with a certain alcohol", choices=(('G', 'Gin'), ('W', 'Whiskey'), ('R', 'Rum'), ('V', 'Vodka'), ('T', 'Tequila'),('N', "Don't Drink"),))

	twitter_id = models.CharField(max_length=60, blank=True, default="", help_text='optional')
	facebook_url = models.CharField(max_length=60, blank=True, default="", help_text='optional')

	#hometown = models.CharField(max_length=30, blank=True )
	adj1 = models.CharField(verbose_name='Adjective to describe you?' , max_length=20, blank=True, default='')
	adj2 = models.CharField(help_text="optional", verbose_name='Second adjective to describe you?' , max_length=20, blank=True, default='')
	adj3 = models.CharField(help_text="optional", verbose_name='Third adjective to describe you?' , max_length=20, blank=True, default='')

	hair = models.BooleanField(verbose_name="Do you have hair on your head?", choices=yes_no)
	sports = models.BooleanField(verbose_name="Would you consider yourself athletic or interested in sports?", choices=yes_no)
	fraternity = models.BooleanField(verbose_name="Are you in a fraternity?", choices=yes_no)
	party = models.BooleanField(verbose_name="Do you like to party?", choices=yes_no)
	novelty = models.BooleanField(verbose_name="Do you like funny gifts?", choices=yes_no)
	dip = models.BooleanField(verbose_name="Do you ever chew tobacco?", choices=yes_no)
	clip_on = models.BooleanField(verbose_name="Does a clip-on bowtie upset you?", choices=yes_no)
	gf = models.BooleanField(verbose_name="Do you have a special someone that you share your Nice Package with on the regular?", help_text="Yes, we're talking about your dick here", choices=yes_no)
	#allow user to suggest their own preference (json?)
