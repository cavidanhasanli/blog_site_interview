from django.contrib import admin
from base_app.models import *
# Register your models here.

admin.site.register(Settings)
admin.site.register(NavbarModel)
admin.site.register(Footer)

admin.site.register(PostModel)
admin.site.register(PostImageModel)
admin.site.register(PostContactModel)
admin.site.register(PostTags)