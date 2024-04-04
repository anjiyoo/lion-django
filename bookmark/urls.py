from django.urls import path
from . import views

# namespace
app_name = 'bookmark'

urlpatterns = [
    path("", views.BookmarkLV.as_view(), name="index"),
    # 제네릭 뷰는 pk로 받음
    path("<int:pk>/", views.BookmarkDV.as_view(), name="detail"),
]