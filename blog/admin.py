from django.contrib import admin
from blog.models import Post

# 데코레이터로 모델 가져오기
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'modify_dt', 'create_dt', 'slug')
    list_filter=("modify_dt",)
    search_fields=('title', 'content')
    prepopulated_fields = {"slug":("title", )}