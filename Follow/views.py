from django.shortcuts import render, redirect
from Signups.models import Signups
from Follow.models import Follow
from django.db.models import Q
# Create your views here.
def follow_view(request):
    try:
        current_users = request.COOKIES['loged_in_user']
    except:
        return redirect("/")
    user_id = Signups.objects.get( useremail= current_users)
    try:
        followed = Follow.objects.filter(current_user = user_id.id)
    except:
        followed = "None"
    try:
        testcookie = request.COOKIES['loged_in_user']
        users = testcookie
    except:
        return redirect("/")

    try:
        get_accounts = Signups.objects.all()
    except:
        pass
    if followed != "None":
        for x in get_accounts:
            for f in followed:
                if x.id == f.followed_account_id:
                    get_accounts = get_accounts.filter(~Q(id = f.followed_account_id))
    context = {
        "title": "Instagram - Follow",
        "users": users,
        "get_accounts":get_accounts,
        "followed": followed
    }
    return render(request, "follow.html", context)

def follow_user_view(request, userid):
    if request.method == 'POST':
        current_users = request.COOKIES['loged_in_user']
        user_id = Signups.objects.get( useremail= current_users)
        account_id = Signups.objects.filter( id = userid).first()
        see_follow = Follow.objects.filter(current_user = user_id.id, followed_account = account_id.id).exists()
        if see_follow:
            return redirect("/follow/")
        else:
            new_follow = Follow(current_user = user_id.id, followed_account = account_id)
            new_follow.save()
    return redirect("/follow/")


def unfollow_view(request, userid):
    if request.method == 'POST':
        current_users = request.COOKIES['loged_in_user']
        user_id = Signups.objects.get( useremail = current_users)
        unfoll = Follow.objects.get(current_user = user_id.id, id = userid)
        unfoll.delete()
    return redirect("/follow/")