from django.contrib import admin
from face.models import Article
from face.models import Page
from face.models import Comment

admin.site.register(Comment)
admin.site.register(Article)
admin.site.register(Page)