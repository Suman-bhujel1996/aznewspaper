from django.contrib import admin

from newspaper.models import Category, Comment, Contact, Newsletter, Post, Tag, UserProfile
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Newsletter)



class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    date_hierarchy = "published_at"
    

admin.site.register(Post, PostAdmin)