from django.contrib import admin
from .models import Usermodel

# Register your models here.
class UsermodelAdmin(admin.ModelAdmin):
    list_display = ['email','first_name', 'last_name',  'nationality']
    fields = ['first_name', 'last_name', 'email','phone_number', 'nationality','password',  'passport', 'is_staff', 'is_superuser', 'is_active']
    # fieldsets = (
    #     ('Head', {'fields':['username', 'status']}),
    #     ('Content', {'fields':['email', 'description']})
    # )
admin.site.register(Usermodel, UsermodelAdmin)