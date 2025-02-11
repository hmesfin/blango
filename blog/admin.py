from django.contrib import admin
from blog.models import Tag, Post, Comment
from blog.models import Tag, Post, Comment, AuthorProfile


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "published_at")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

admin.site.register(AuthorProfile)
