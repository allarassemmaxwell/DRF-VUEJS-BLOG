from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy      = 'published'
    list_display 		= ['title', 'author', 'published']
    list_display_links 	= ['title']
    list_filter 		= ['title', 'published']
    search_fields 		= ['title', 'published']
    readonly_fields		= ['published']
    list_per_page 		= 25
    class Meta:
        model = Post
admin.site.register(Post, PostAdmin)