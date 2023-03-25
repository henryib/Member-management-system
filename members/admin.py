from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Member
from import_export import resources

#import export functionality

class MemberResource(resources.ModelResource):
    class Meta:
        model = Member

class MemberAdmin(ImportExportModelAdmin): 
    pass

# Register your models here.
admin.site.register(Member, MemberAdmin)







