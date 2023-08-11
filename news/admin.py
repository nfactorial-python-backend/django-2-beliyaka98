from django.contrib import admin
from .models import New, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5

class NewAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at", "has_comments"]
    inlines = [CommentInline,]



admin.site.register(New, NewAdmin)
admin.site.register(Comment)