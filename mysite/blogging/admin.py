from django.contrib import admin

from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    # Include all default post fields
    exclude = ()
    # Add categories
    inlines = [
        CategoryInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)