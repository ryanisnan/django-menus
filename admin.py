from django.contrib import admin
from menus.models import Menu, MenuCategory, MenuItem, ImportantIngredient

admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(ImportantIngredient)