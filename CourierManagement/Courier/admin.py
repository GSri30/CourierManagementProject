from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('FromName','CourierId','Collected','Received_On')
    list_filter = ('FromName','Collected')
    search_fields = ['FromName','CourierId', 'StudentName','RollNumber','Mobile','Email']

admin.site.register(Post,PostAdmin)