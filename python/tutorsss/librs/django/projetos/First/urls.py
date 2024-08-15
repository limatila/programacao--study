"""
URL configuration for First project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse as HTTP


"""
* Here will be registered all URLs for the
* server to respond to page access.
* Accesses are Requests, the Server responds in HttpResponse(s)
* each Respons can be mounted in a
* view (a def that returns a HttpResponse)
TODO: search include()
"""


def home_view(request):
    return HTTP("""
<h1>Bem Vindo</h1>
<a href="">1. Reclame Aqui</a>""")


def root_view(request):
    return HTTP("CHOOSE: /admin/  --  /home/")


urlpatterns = [  # * all available URLs. Apply 'path(url, view, other args)'
    path('', root_view, name="Root page"),
    path('home/', home_view, name="Home"),
    path('admin/', admin.site.urls),
]
