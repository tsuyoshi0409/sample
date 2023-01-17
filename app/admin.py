from django.contrib import admin

from .models import *

admin.site.register(Material)
admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Part)
admin.site.register(Operation)
admin.site.register(ChildOperation)
admin.site.register(Bell)