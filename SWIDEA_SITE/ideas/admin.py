from django.contrib import admin
from .models import Idea, DevTool, IdeaStar

# Register your models here.
admin.site.register(Idea)
admin.site.register(DevTool)
admin.site.register(IdeaStar)
