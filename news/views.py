from django.shortcuts import render, get_object_or_404, redirect

from .models import New, Comment

def news(request):
    data_news = New.objects.all().order_by("-created_at")
    return render(request, "news/news.html", {"news": data_news})

def detail(request, id):
    data_new = get_object_or_404(New, id=id)
    if request.method == "POST":
        comment_new = Comment(content=request.POST["content"], new=data_new)
        comment_new.save()
        return redirect("detail", id=data_new.id)
    return render(request, "news/detail.html", {"new": data_new})

def create_new(request):
    if request.method == 'POST':
        data_new = New(title=request.POST["title"], content=request.POST["content"])
        data_new.save()
        return redirect("detail", id=data_new.id)
    return render(request, "news/create.html")