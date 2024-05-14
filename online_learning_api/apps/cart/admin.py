from django.contrib import admin
from .models import Cart
# Register your models here.
admin.site.register(Cart)
admin.site.site_header = '在学商城后台管理系统'
admin.site.site_title = '在学商城后台管理系统'
admin.site.index_title = '在学商城后台管理系统'