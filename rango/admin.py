from django.contrib import admin
from rango.models import Category, Page, UserProfile
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields':['category', 'title']}),
    #     ('The link', {'fields':['url']}),
    #     ('View times', {'fields':['views']})
    # ]
    list_display = ('category', 'title', 'url', 'views')
    

class CategoryAdmin(admin.ModelAdmin):
    prepopulate_fields = {'slug':('name',)}
    list_display = ('name', 'views', 'likes')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

