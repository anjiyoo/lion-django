from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

class PostLV(ListView):
    model = Post
    # 템플릿 연결
    template_name = "blog/post_all.html"  # default : blog/post_list.html
    # 보여줄 객체
    context_object_name = 'posts'
    # 내용 한개를 한 페이지로 구성
    paginate_by = 1


class PostDV(DetailView):
    model = Post
    # 템플릿 연결
    template_name = "blog/post_detail.html"


#--- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive.html"


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    template_name = "blog/post_archive_year.html"



class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive_month.html"



class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive_day.html"



class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive_day.html"