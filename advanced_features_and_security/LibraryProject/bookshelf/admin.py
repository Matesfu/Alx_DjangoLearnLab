from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book
from .models import CustomUser
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # fieldsets controls what you see in the "Change User" page
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # add_fieldsets controls what you see in the "Add User" page
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )


admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)