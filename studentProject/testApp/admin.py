from django.contrib import admin

# Register your models here.
from testApp.models import Students
class StudentAdmin(admin.ModelAdmin):
    list_display=['Image']

admin.site.register(Students,StudentAdmin)
