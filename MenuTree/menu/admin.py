from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from .models import *


class MenuAdminForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'parent']

    def clean_parent(self):
        parent = self.cleaned_data['parent']
        if self.instance.nesting_level == 0 and parent:
            raise ValidationError("Нельзя выбрать родителя для корневого меню.")
        if parent == self.instance:
            raise ValidationError("Нельзя выбрать текущее меню в качестве родителя.")
        return parent


class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm
    list_display = ['name', 'parent', 'nesting_level', 'slug']


admin.site.register(Menu, MenuAdmin)
