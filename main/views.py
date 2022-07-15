from django.shortcuts import render, redirect, HttpResponse
from .models import Post
from .form import PostForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def MainIndex(request):
    sarlavha = _("Bosh sahifa")
    return render(request, "index.html", context={
        "page_title": sarlavha,
        "objects_list": Post.objects.all()
    })


def Maintech(request):
    sarlavha = _("Sci-Fi")
    return render(request, "tech.html", context={
        "page_title": sarlavha
    })


def MainShow(request):
    sarlavha = _("Tv Showlar")
    return render(request, "show.html", context={
        "page_title": sarlavha
    })


def Mfilm(request):
    sarlavha = _("Filmlar")
    return render(request, "mfilm.html", context={
        "page_title": sarlavha
    })


def MainReg(request):
    sarlavha = _("Ro'yhatdan o'tish")
    return render(request, "account/registration.html", context={
        "page_title": sarlavha
    })


def MainFilm(request):
    sarlavha = "Film"
    return render(request, "film.html", context={
        "page_title": sarlavha
    })


def MainPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, _("Muvaffaqiyatli qo'shildi!"))

            return redirect('main:index')

    return render(request, 'main/add.html', {
        'form': form,
        "page_title": _("Maqola qo'shish")
    })


def main_delete_post(request, id):
    Post.objects.filter(id=id).delete()

    messages.success(request, _("Maqola o'chirildi!"))
    return redirect('main:index')


def main_view(request, id):
    post = Post.objects.get(id=id)

    request.breadcrumb = [
        post.subject
    ]
    return render(request, 'main/view.html', {
        'post': post
    })