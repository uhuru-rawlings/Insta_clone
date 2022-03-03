from django.shortcuts import render, redirect
from Profiles.models import Imageuploads, Likes, Comments
from Signups.models import Signups

# Create your views here.
def home_view(request):
    try:
        likes = Likes.objects.all()
    except:
        likes = "nolikes"
    try:
        comms = Comments.objects.all()
    except:
        comms = "nocomms"
    try:
        posts = Imageuploads.objects.all()
    except:
        posts = "Youhavenocurrentpost"
    try:
        testcookie = request.COOKIES['loged_in_user']
        users = testcookie
    except:
        return redirect("/")
    context = {
        "users": users,
        "title":"Instagram",
        "posts": posts,
        "comms":comms,
        "likes":likes
    }
    return render(request, "home.html", context)

def comments_view(request, post_id):
    if request.method == 'POST':
        current_user = request.COOKIES['loged_in_user']
        get_user = Signups.objects.get(useremail=current_user)
        comment = request.POST['comments']
        get_post = Imageuploads.objects.get(id = post_id)
        new_comment = Comments(post_id=get_post, comment_by=get_user, comment_post=comment)
        new_comment.save()

    return redirect("/home/")

def likes_view(request, post_id):
    if request.method == 'POST':
        current_user = request.COOKIES['loged_in_user']
        liked_by = Signups.objects.get(useremail=current_user)
        liked_post = Imageuploads.objects.get(id = post_id)
        new_likes = Likes(post_id=liked_post, liked_by= liked_by)
        new_likes.save()

    return redirect("/home/")