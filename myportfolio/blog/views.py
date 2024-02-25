from django.shortcuts import render
from .models import Post, Comment
from blog.forms import CommentForm, ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})


def blog_category(request, category):
    posts = Post.objects.filter(categories__name=category).order_by("-date_created")
    return render(request, "blog/category.html", {"category": category, "posts": posts})

def post_detail(request, pk):
    post = Post.objects.get(pk = pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments": comments, "form": form}
    comments = Comment.objects.filter(post = post)
    return render(request, "blog/post_detail.html", context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f'message from {name}'
            body = f"Email: {email}\n\nMessage:\n{message}"
            sender_mail = 'baseedmaena@gmail.com'

            send_mail(subject, body, sender_mail, ['baseedmaena@gmail.com'])
            return render(request, 'blog/success_template.html')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})
