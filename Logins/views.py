from django.shortcuts import render, redirect, HttpResponse
from Signups.models import Signups
# Create your views here.
def login_view(request):
    errors = ""
    # try:
    #     request.COOKIES['loged_in_user']
    #     return redirect("/home/")
    # except:
    #     pass
    if request.method == 'POST':
        useremails = request.POST['useremails']
        passsword = request.POST['passwords']
        if Signups.objects.filter(useremail = useremails).exists():
            get_user = Signups.objects.get(useremail = useremails)
            if(get_user.password == passsword):
                response = redirect("/home/")
                response.set_cookie("loged_in_user",useremails)
                return response
                # return redirect("home/")
            else:
                errors = "Wrong password please try again"
        else:
            errors = "User with this email do not exist"
    context = {
        "title": "Instagram - Login",
        "error": errors
    }
    return render(request, "index.html", context)


