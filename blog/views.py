from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm
# Create your views here.

"""
This contains three views:
-blog_index: holds view for the index page of
 the blog. It displays all Posts on the blog.

-blog_detail: contains all the posts as well as
comments and a form to allow new users to 
create new comments.

-blog_category: displays blogs of a specific category
 as chosen by the user.
"""

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts' : posts,
    }
    return render(request, 'blog_index.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=blog_category
    ).order_by(
        '-created_on'
    )
    context = {
        'category' : category,
    'post' : posts,
    }
    return render(request, 'blog_category.html', context)

def blog_detail(request, pk):
    # Retrieval of post objects
    post = Post.objects.get(pk=pk)

    #Instantiation of form object
    form = CommentForm()

    # Checking if it's a post request
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        # testing for form validity
        if form.is_valid():
            comment = Comment(
                # Accessing of form data after validity check
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post=post
            )
            # Save post comment
            comment.save()

    # Filter object based on post during retrieval
    comments = Comment.objects.filter(post=post)
    
    # Context for rendering in template
    context = {
        'post' : post,
        'comments' : comments,
        'form': form,
    }
    return render(request, 'blog_detail.html', context)
