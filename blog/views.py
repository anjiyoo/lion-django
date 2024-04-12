from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView, TemplateView, FormView
from django.conf import settings
from blog.forms import PostSearchForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# ListView : 전체적인 데이터 보여줌
class PostLV(LoginRequiredMixin, ListView):
    model = Post
    # 템플릿 연결
    template_name = "blog/post_all.html"  # default : blog/post_list.html
    # 보여줄 객체
    context_object_name = 'posts'
    # 내용 한개를 한 페이지로 구성
    paginate_by = 3
    # 로그인 화면으로 연결(필수x)
    login_url = '/accounts/login/'
    # # 데이터 가져오기 (필터링 가능 ex)최근 5개 데이터 가져오기)
    # def get_queryset(self):
    #     return Post.objects.all()
    
# # PostLV 와 같은 기능   
# def dumppy_post(request):
#     object = Post.objects.all()
#     context = {
#         'posts' : object
#     }
#     return render(request, 'blog/post_all.html', context)


# DetailView : 특정 항목 하나를 보여줌
class PostDV(DetailView):
    model = Post
    # 템플릿 연결
    template_name = "blog/post_detail.html"
    # get_queryset -> get_object에서 id나 pk나 가져옴
    # def get_object(self):pass
    # DISQUS 데이터 보내기
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context


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


# TAG
class TagCloudTV(TemplateView):
    template_name="taggit/taggit_cloud.html"

class TaggedObjectLV(ListView):
    template_name='taggit/taggit_post_list.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
    # post_list.html에 넘겨줄 컨텍스트 변수 추가하는 메소드
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
    

# SEARCH
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form: Any) -> HttpResponse:
        # 검색어 확인
        searchWord = form.cleaned_data['search_word']
        # Q를 통해 검색하고
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()
        # 결과를 담아
        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        # 페이지에 전달
        return render(self.request, self.template_name, context)
