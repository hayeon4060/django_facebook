from django.shortcuts import render, redirect
from django.http import HttpResponse
from face.models import Article
from face.models import Page
from face.models import Comment
# from face.models import new_feed
# from face.models import edit_feed
# from face.models import remove_feed

def play(request):
   return render(request, 'play.html')
  # return HttpResponse("hello")

count = 0
def play2(request):
       
   return render(request, 'play2.html')
   # age=20
   # leehayeon="이하연"
   # global count
   # count = count + 1

   # if age > 19:
   #       status='성인'
   # else:
   #       status='청소년'

   # diary = ['오늘은 날씨가 맑았다. -4월 3일', '미세먼지가 너무 심하다. (4월 2일)', '비가온다. 4월 1일에 작성']


   # return render(request, 'play2.html', { 'name': leehayeon, 'diary':diary, 'cnt':count, 'age':status })

def my_profile(request):
   return render(request, 'profile.html')

def event(request):
   leehayeon='이하연'
   age=20
   global count
   count+=1
   if age>19:
          status='성인'
   else:
          status='cjdthsus'



   if count==7:
          result='당첨! 입니다'
   else:
          result='꽝...입니다.'
   return render(request, 'event.html', {'name': leehayeon, 'age':age, 'cnt':count, 'result': result})

def fail(request):
       return render(request, 'fail.html')
def help(request):
       return render(request, 'help.html')
def warn(request):
       return render(request, 'warn.html')

def newsfeed(request):
       articles=Article.objects.all()
       return render(request, 'newsfeed.html', { 'articles': articles })

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':  # new comment
        Comment.objects.create(
            article=article,
            author=request.POST['nickname'],
            text=request.POST['reply'],
            password=request.POST['password']
        )

        return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html', {'feed': article})

def pages(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages })


def new_feed(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            text = request.POST['content']
            text = text + ' - 추신: 감사합니다.'

            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=text,
                password=request.POST['password']
            )

            # 새글 등록 끝
            return redirect(f'/feed/{ new_article.pk }')

    return render(request, 'new_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/') # 첫페이지로 이동하기

        else:
            return redirect('/fail/')  # 비밀번호 오류 페이지 이동하기

    return render(request, 'remove_feed.html', {'feed': article})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')
        else:
            return redirect('/fail/')  # 비밀번호 오류 페이지 이동하기

    return render(request, 'edit_feed.html', {'feed': article})


def new_page(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        new_page = Page.objects.create(
            master=request.POST['master'],
            name=request.POST['name'],
            text=request.POST['text'],
            category=request.POST['category']
        )

        # 새 페이지 개설 완료
        return redirect('/pages/')

    return render(request, 'new_page.html')

def remove_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.delete()
        return redirect('/pages/')

    return render(request, 'remove_page.html', {'page': page})

def edit_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.master = request.POST['master']
        page.name = request.POST['name']
        page.text = request.POST['text']
        page.category = request.POST['category']
        page.save()
        return redirect('/pages/')

    return render(request, 'edit_page.html', {'page': page })


def remove_comment(request, pk,commentpk):
    comment = Comment.objects.get(pk=commentpk)

    if request.method == 'POST':
        if request.POST['password'] == comment.password:
            comment.delete()
            return redirect('../../../') 

        else:
            return redirect('/fail/')  # 비밀번호 오류 페이지 이동하기

    return render(request, 'remove_comment.html', {'comment': comment})
