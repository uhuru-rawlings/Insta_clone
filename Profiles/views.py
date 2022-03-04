from django.shortcuts import render, redirect
from Profiles.models import Biog, Imageuploads
from Signups.models import Signups

# Create your views here.
def profile_view(request):
    try:
        current_users = request.COOKIES['loged_in_user']
    except:
        return redirect("/")
    userid = Signups.objects.filter(useremail = current_users)
    mydetails = Signups.objects.filter( useremail = current_users).first()
    try:
        posts = Imageuploads.objects.filter(profile = mydetails.id)
    except:
        posts = "Nopost"
    try:
        getbios = Biog.objects.filter(user_id = mydetails.id).first()
        bioinfo = getbios
    except:
        bioinfo = "notbio"
    try:
        testcookie = request.COOKIES['loged_in_user']
        users = testcookie
    except:
        return redirect("/")
    context = {
        "title": "Instagram - Profile",
        "users": users,
        "mydetails":mydetails,
        "bioinfo": bioinfo,
        "posts":posts
    }
    return render(request, "profile.html", context)

def add_bio_view(request, profile_id):
    current_users = request.COOKIES['loged_in_user']
    userid = Signups.objects.get( useremail= current_users)
    if request.method == 'POST':
        user_bio = request.POST['userbio']
        get_bio = Biog.objects.filter(user_id = userid.id).exists()
        get_bios = Biog.objects.filter(user_id = userid.id)
        new_bio = Biog(user_id = userid, user_bio = user_bio)
        if get_bio:
            get_bios.update(user_bio = user_bio)
        else:
            new_bio.save()
    return redirect("/profile/")


def uploadimages(request):
    if request.method == 'POST':
        current_users = request.COOKIES['loged_in_user']
        get_current = Signups.objects.get(useremail=current_users)
        uploadefile = request.FILES['imagefiles']
        imagecaption = request.POST['imagecaptions']
        new_post = Imageuploads(image_name = uploadefile,image_caption = imagecaption, profile = get_current)
        new_post.save()
    return redirect("/home/")