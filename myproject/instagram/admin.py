from django.contrib import admin
from django.db.models import fields
from .models import PostModel, ImagePostModel

# Register your models here.
admin.site.site_header = 'Instagram'

class PostModelAdmin(admin.ModelAdmin):
    list_filter = ('id', 'detail', 'date_update')
    list_display = ('id', 'date_update')
    fieldsets = [
        (None, {'fields' : ['detail']}),
        ('Automatic', {'fields':['date_create','date_update']})
    ]
    readonly_fields = ['date_create', 'date_update']

    class Meta:
        model = PostModel
        fields = '__all__'
        
        

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(ImagePostModel)