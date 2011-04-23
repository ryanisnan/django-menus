from django.db import models

class Menu(models.Model):
	name = models.CharField(max_length=24, unique=True, verbose_name='menu name')
	order = models.PositiveSmallIntegerField(default=0, help_text='The order of the menu determines where this menu appears alongside other menus.')
	
	class Meta:
		ordering = ['order']

class MenuCategory(models.Model):
	menu = models.ForeignKey(Menu, help_text='The menus that this category belongs to, i.e. \'Lunch\'.') 
	name = models.CharField(max_length=32, verbose_name='menu category name')
	additional_text = models.CharField(max_length=128, null=True, blank=True, help_text='The additional text is any bit of related information to go along with a menu category, i.e. the \'Pasta\' category might have details that say \'All entrees come with salad and bread\'.')
	order = models.IntegerField(default=0, help_text='The order is the order that this category should appear in when rendered on the templates.')
	
	class Meta:
		verbose_name='menu category'
		verbose_name_plural='menu categories'
		ordering = ['order', 'name']
	
	def __unicode__(self):
		return self.name

class ImportantIngredient(models.Model):
	name = models.CharField(max_length=16, unique=True, help_text='ingredient name, i.e. \'Gluten\', or \'Peanuts\'.')

	class Meta:
		verbose_name='important ingredient'
		verbose_name_plural='important ingredients'

	def __unicode__(self):
		return self.name

class MenuItem(models.Model):
	CLASSIFICATION_CHOICES = (
		('neither', 'Neither'),
		('vegan', 'Vegan'),
		('vegetarian', 'Vegetarian'),
	)

	name = models.CharField(max_length=48, help_text='Name of the item on the menu.')
	description = models.CharField(max_length=128, null=True, blank=True, help_text='The description is a simple text description of the menu item.')
	price = models.IntegerField(help_text='The price is the cost of the item.')
	category = models.ManyToManyField(MenuCategory, verbose_name='menu category', help_text='Category is the menu category that this menu item belongs to, i.e. \'Appetizers\'.')
	order = models.IntegerField(default=0 verbose_name='order', help_text='The order is to specify the order in which items show up on the menu.')
	image = models.ImageField(upload_to='menu', null=True, blank=True, verbose_name='image', help_text='The image is an optional field that is associated with each menu item.')
	spicy = models.BooleanField(default=False, verbose_name='spicy?', help_text='Is this item spicy?')
	classification = models.CharField(max_length=10, choices=CLASSIFICATION_CHOICES, default=0, verbose_name='classification', help_text='Select if this item classifies as Vegetarian, Vegan, or Neither.')
	important_ingredients = models.ManyToManyField(ImportantIngredient, null=True, blank=True, verbose_name='important ingredients', help_text='This is the list of ingredients that this item contains that are important to customers, such as \'Gluten\' or \'Peanuts\'.')
	
	class Meta:
		verbose_name='menu item'
		verbose_name_plural='menu items'
		ordering = ['category', 'order', 'name']

	def __unicode__(self):
		return self.name