from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm
# Create your views here.

def BlogIndex(request):
    o_Posts = Post.objects.all().order_by('-d_Creation')
    ctx = {
        "o_Posts": o_Posts,
    }
    return render(request, "BlogIndex.html", ctx)

def BlogCategory(request, o_Category):
    o_Posts = Post.objects.filter(o_Categories__s_Name__contains=o_Category).order_by('-d_Creation')
    ctx = {
        "o_Category": o_Category,
        "o_Posts"   : o_Posts,
    }
    return render(request, "BlogCategory.html", ctx)

def BlogDetail(request, pk):
    o_Post      = Post.objects.get(pk=pk)
    o_Form      = CommentForm()
    if request.method == 'POST':
        o_Form = CommentForm(request.POST)
        if o_Form.is_valid():
            o_Comment = Comment(
                s_Author = o_Form.cleaned_data["s_Author"],
                s_Body   = o_Form.cleaned_data["s_Body"],
                o_Post   = o_Post
            )
            o_Comment.save()

    o_Comments  = Comment.objects.filter(o_Post=o_Post)

    ctx = {
        "o_Post"    : o_Post,
        "o_Comments": o_Comments,
        "o_Form"    : o_Form
    }

    return render(request, "BlogDetail.html", ctx)
