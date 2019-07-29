from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost


def home(request):
    blogs = Blog.objects   # 모델로부터 객체 목록을 전달 받을 수 있음 .objects, 객체목록을 쿼리셋이라고 함. 쿼리셋을 활용하게끔 해주는게 메소드!
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드


def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)  # pk는 객체들의 이름표, 구분자, 데이터의 대표값
    # 어떤 클래스로 부터, 몇 번 객체를 받아줄지 를 위해 인자 2개 받음
    return render(request, 'detail.html', {'details': details})


def new(request):                # new.html을 띄워주는 함수
    return render(request, 'new.html')


def create(request): # 입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()  # 쿼리셋 메소드 중 하나인데 블로그라고 하는 객체를 DB에 저장하라!
    return redirect('/blog/'+str(blog.id))   # URL은 항상 문자열!
    # redirect 함수는 아무 url이나 가능


def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 --> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)  # 입력된 내용을 담아준 것!
        if form.is_valid():   # 이것 때문에 입력을 안하고 제출을 하면 이 입력란을 작성하시오! 라는 말이 뜨는 것!
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 2. 빈 페이지를 띄워주는 기능 --> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form': form})
