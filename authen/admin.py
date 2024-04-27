from django.contrib import admin
from django import forms
from .models import KeyActive
from flow_manager.models import FLow

class KeyActiveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hiển thị tên của dự án thay vì ID trong trường "project"
        self.fields['project'].queryset = FLow.objects.all()
        self.fields['project'].label_from_instance = lambda obj: "%s" % obj.name

class KeyActiveAdmin(admin.ModelAdmin):
    filter_horizontal = ('project',)  
    list_filter = ('project',)  
    list_display = ('name','id')
    search_fields = ['name', 'id']  
    form = KeyActiveForm

admin.site.register(KeyActive, KeyActiveAdmin)
