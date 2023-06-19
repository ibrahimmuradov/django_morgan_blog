from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from urllib.parse import urlparse
from .models import Blog, BlogImage, Category, Comment
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

user = get_user_model()


def index(request):
    blogs = Blog.objects.filter(status='Active')
    head_blogs = Blog.objects.filter(status='Active')[:8]

    filter_, filter_dict = Q(), {}

    category = request.GET.getlist("category", None)

    if category != "" and category:
        filter_dict["category"] = "".join(f'category={cat}&' for cat in category)
        filter_.add(Q(category__in=category), Q.AND)


    tag = request.GET.getlist("tag", None)

    if tag != "" and tag:
        filter_dict["tag"] = "".join(f'tag={cat}&' for cat in tag)
        filter_.add(Q(tags__in=tag), Q.AND)


    if request.method == "POST" and 'search' in request.POST:
        search = request.POST.get('search')
        filter_dict["search"] = search
        filter_.add(Q(title__icontains=search), Q.AND)

    blogs = blogs.filter(filter_)

    paginator = Paginator(blogs, 6)
    page = request.GET.get('page', 1)
    blog_list = paginator.get_page(page)

    context = {
        'blogs': blog_list,
        'head_blogs': head_blogs,
        "categories": Category.objects.filter(parent__isnull=True),
        'paginator': paginator,
        "filter_dict": filter_dict.values()
    }

    return render(request, 'blog/index.html', context)


def post(request, id):
    get_blog = get_object_or_404(Blog, id=id)

    get_blog.view_count += 1
    get_blog.save()

    comments = Comment.objects.filter(Q(parent__isnull=True)&(Q(blog=get_blog.id))).order_by('-created_at')

    get_user = None

    if request.user.username:
        get_user = user.objects.get(username=request.user.username) if user.objects.filter(
            username=request.user).exists() else None

    count_comment = get_blog.comment_set.filter(Q(user=get_user)&Q(parent__isnull=True)).count()
    count_reply_comment = get_blog.comment_set.filter(Q(user=get_user)&Q(parent__isnull=False)).count()

    if request.method == "POST" and "comment" in request.POST:
        comment = request.POST.get("comment")

        if count_comment < 3:
            Comment.objects.create(
                user=get_user,
                blog=get_blog,
                message=comment
            )

            return redirect('blog:post', get_blog.id)

    elif request.method == "POST" and "reply-comment" in request.POST:
        reply_comment = request.POST.get("reply-comment")
        parent_comment = Comment.objects.get(id=request.POST.get('reply-comment-id'))

        if count_reply_comment < 3:
            Comment.objects.create(
                user=get_user,
                parent=parent_comment,
                blog=get_blog,
                message=reply_comment
            )

            return redirect('blog:post', get_blog.id)

    context = {
        'blog': get_blog,
        "categories": Category.objects.filter(parent__isnull=True),
        'comments': comments
    }

    return render(request, 'blog/blog-single.html', context)

@login_required(login_url="/user/login/")
def delete_comment(request):
    data = {}
    get_object_or_404(user, username=request.user)

    comment = get_object_or_404(Comment, id=int(request.POST.get("commentID")))

    get_user = user.objects.get(username=request.user)

    if comment.user == get_user:
        comment.delete()
        data["success"] = True
    else:
        data["success"] = False

    return JsonResponse(data)


def about(request):
    context = {}
    return render(request, 'blog/about.html', context)


def base(request):
    url = request.POST.get('url')
    parsed_url = urlparse(url)
    path = parsed_url.path.strip('/')

    get_user = False

    if request.user.username:
        get_user = True if user.objects.filter(
            username=request.user).exists() else False

    data = {
        'user': get_user,
        'path': 'home' if path == "" else path
    }

    return JsonResponse(data)
