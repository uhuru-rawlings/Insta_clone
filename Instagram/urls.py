"""Instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Logins.views import login_view
from Signups.views import signup_view
from Home.views import home_view, comments_view,likes_view, search_view
from Follow.views import follow_view, follow_user_view, unfollow_view
from Profiles.views import profile_view, add_bio_view, uploadimages
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name = "Login"),
    path('signup/', signup_view, name = "Signup"),
    path('home/', home_view, name = "home"),
    path('search/', search_view, name = "searchresults"),
    path('comment/<int:post_id>/', comments_view, name = "comments"),
    path('like/<int:post_id>/', likes_view, name = "likes"),
    path('follow/', follow_view, name = "follow"),
    path('unfollow/<int:userid>/', unfollow_view, name = "unfollow"),
    path('profile/', profile_view, name = "profiles"),
    path('addbio/<int:profile_id>/', add_bio_view, name = "biography"),
    path('followed/<int:userid>/', follow_user_view, name = "followed"),
    path('uploadimages/', uploadimages, name = "uploadimages"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)