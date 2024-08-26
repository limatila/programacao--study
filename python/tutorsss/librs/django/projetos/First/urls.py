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
from django.urls import path, include


"""
* Here will be registered all URLs for the
* server to respond to page access.
* Accesses are Requests, the Server responds in HttpResponse(s)
* each Response can be mounted in a
* view (a def that returns a HttpResponse)
* outside, in view.py in an created App
* Include: bring URLs especifications from the individual App.
"""


urlpatterns = [  # * all available URLs. Apply 'path(url, view, other args)'
    path('admin/', admin.site.urls),
    path('reclame-aqui/', include('ReclameAqui.urls')),
    path('', include('Receitas.urls'))
]
