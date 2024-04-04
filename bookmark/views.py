from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# listview를 사용해 전체 보이기
class BookmarkLV(ListView):
    model = Bookmark

    # # 아래 내용 디폴트로 지정됨
    # template_name = "bookmark/bookmark_list.html"  # appname/model_name_list.html
    # context_object_name = "object_list"  # object_list


# detailview 만들기
class BookmarkDV(DetailView):
    model = Bookmark

    # template_name="bookmark/bookmark_detail.html"  # appname/model_name_detail.html
    # context_object_name = "object"  # object
