from django.contrib import admin

from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Include all default post fields
    exclude = ()
    # Add categories
    inlines = [
        CategoryInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
