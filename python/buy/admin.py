from django.contrib import admin
from .models import Blog,Author,User_register,Image


admin.site.register(Blog)
# admin.site.register(Author)
# Register your models here.



class author_(admin.ModelAdmin):
    list_display = ['name','email']
    list_filter  = ['email']
    search_fields = ['name','email']


admin.site.register(Author,author_)    


class userregister(admin.ModelAdmin):
    list_display =['name','email','Password','address']


admin.site.register(User_register,userregister) 


class Image_(admin.ModelAdmin):
    list_display =['image']

admin.site.register(Image,Image_)    