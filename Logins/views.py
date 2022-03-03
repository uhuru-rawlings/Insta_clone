from django.shortcuts import render, redirect, HttpResponse
from Signups.models import Signups
# Create your views here.
def login_view(request):
    errors = ""
    if request.method == 'POST':
        useremails = request.POST['useremails']
        passsword = request.POST['passwords']
        if Signups.objects.filter(useremail = useremails).exists():
            get_user = Signups.objects.get(useremail = useremails)
            if(get_user.password == passsword):
                response = HttpResponse('home')
                setcooke = response.set_cookie("loged_in_user",useremails)
                if setcooke:
                    return [response,redirect("home/")]
                else:
                     errors = "Failed to set login required details"
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

def send_home():
    return redirect("home/")