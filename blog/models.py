from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    # CharField(max_length) 지정해야 에러 안남
    title = models.CharField(verbose_name='TITLE', max_length=50)
    # slug : 제목 별칭
    slug = models.SlugField(verbose_name="SLUG", unique=True, allow_unicode=True, help_text="one word for title alias.")
    description = models.CharField("DESCRIPTION", max_length=100, blank=True, help_text="simple text")
    content = models.TextField("CONTENT")
    # 생성일
    create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True)
    # 수정일
    modify_dt = models.DateTimeField("MODIFY DATE", auto_now=True)
    # 태그
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering=('-modify_dt',)  # - : 내림차순(최신내용 맨 위)

    def __str__(self):
        return self.title
    # 메소드가 정의된 객체를 지칭하는 url 반환
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug, ))
    # get_previous메소드 : 장고 내장 함수 호출. modify_dt를 기준으로 최신 포스트를 먼저 보여줌
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    # get_previous메소드 : 장고 내장 함수 호출.modify_dt를 기준으로 다음 포스트 반환
    def get_next(self):
        return self.get_next_by_modify_dt()
    
# # Comment
# class Comment(models.Model):
#     # user <- 사용자테이블 있을 때
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     Comment = models.CharField(max_length=200)

