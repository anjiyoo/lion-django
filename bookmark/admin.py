from django.contrib import admin
from bookmark.models import Bookmark

# # 모델 가져오기
# admin.site.register(Bookmark)

# 데코레이터로 모델 가져오기
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'url')