from django.shortcuts import render, redirect
from Profiles.models import Imageuploads, Likes, Comments
from Signups.models import Signups
from Follow.models import Follow

# Create your views here.
def home_view(request):
    try:
        current_users = request.COOKIES['loged_in_user']
    except:
        return redirect("/")
    user_id = Signups.objects.get( useremail = current_users)
    try:
        followed = Follow.objects.filter(current_user = user_id.id)
    except:
        followed = "None"
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
    alllikes = []
    if posts != "Youhavenocurrentpost":
        for post in posts:
            getlike = Likes.objects.filter(post_id = post.id)
            alllikes.append({"postid":post.id, "likes": getlike.count()})

    context = {
        "users": users,
        "title":"Instagram",
        "posts": posts,
        "comms":comms,
        "likes":likes,
        "followed":followed,
        "alllikes":alllikes
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
        try:
            likes = Likes.objects.get(post_id=liked_post, liked_by= liked_by)
            likes.delete()
        except:
            new_likes = Likes(post_id=liked_post, liked_by= liked_by)
            new_likes.save()
# function(a,b){a - b} => this is ana  anonymous function
    return redirect("/home/")

def search_view(request):
    if request.method == 'POST':
        username = request.POST['searchitems']
        try:
            profile = Signups.objects.filter(username=username).first()
        except:
            return redirect("/home/")
        try:
            posts = Imageuploads.objects.filter(profile_id = profile.id).order_by("-id")
        except:
            posts = "nopost" 
        likes = Likes.objects.all()
        try:
            comms = Comments.objects.all()
        except:
            comms = "nocomms"

        alllikes = []
        outcome = ''
        if posts != "nopost":
            for post in posts:
                getlike = Likes.objects.filter(post_id = post.id)
                if getlike:
                    alllikes.append({"postid":post.id, "likes": getlike.count()})
                else:
                    outcome = "nopost"
            else:
                outcome = "nopost"
        context = {
            "usernames":username,
            "posts":posts,
            "profile":profile,
            "likes":likes,
            "comms":comms,
            "alllikes":alllikes,
            "outcome":outcome
        }
        return render(request, "search.html", context)