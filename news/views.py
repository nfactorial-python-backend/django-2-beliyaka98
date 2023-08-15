from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import New, Comment
from .forms import NewsForm

def news(request):
    data_news = New.objects.all().order_by("-created_at")
    return render(request, "news/news.html", {"news": data_news})

def detail(request, id):
    data_new = get_object_or_404(New, id=id)
    if request.method == "POST":
        comment_new = Comment(content=request.POST["content"], new=data_new)
        comment_new.save()
        return redirect("detail", id=data_new.id)
    context = {"new": data_new, "comments": data_new.comment_set.all().order_by("-created_at")}
    return render(request, "news/detail.html", context = context)

def create_new(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("detail", id=form.instance.id)
    form = NewsForm()
    return render(request, "news/create.html", {"form": form})

class EditView(View):
    def get(self, request, id: int):
        new = get_object_or_404(New, id=id)
        form = NewsForm(instance=new)
        return render(request, "news/edit.html", {"form": form})
    def post(self, request, id: int):
        new = get_object_or_404(New, id=id)
        form = NewsForm(request.POST, instance=new)
        if form.is_valid():
            form.save()
            return redirect("detail", id=form.instance.id)