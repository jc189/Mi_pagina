from django.contrib import admin
from .models import Post
from .models import PostTwo

admin.site.register(Post)
admin.site.register(PostTwo)