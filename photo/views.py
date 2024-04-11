from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Album, Photo

class AlbumLV(ListView):
    model = Album
    # ListView의 기본 템플릿 : 앱이름/모델_list.html
    template_name = 'photo/album_list.html'
    # def get_queryset(self) -> QuerySet[Any]:
    #     # Album 안의 objects 모두 가져오기
    #     return self.model.objects.all()
    # def get_objects : DetailView에서 사용
    # def get_context_data : 다른 값들도 가져올 수 있는 메소드

# pk를 통해서 특정 앨범만 가져옴
class AlbumDV(DetailView):
    model = Album
    template_name = 'photo/album_detail.html'

class PhotoDV(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'
