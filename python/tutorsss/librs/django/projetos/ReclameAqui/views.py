from django.http import HttpResponse as HTTP
from django.http import HttpResponseForbidden

from django.shortcuts import render


def home(request):
    return render(request, "home.html", content_type="text/html")


def root_view(request):
    return HTTP("CHOOSE: /admin/  --  /home/  --  /contato/")


def contato(request):
    # ? trying usage of request attributes
    if "text/html" in request.META["HTTP_ACCEPT"]:
        return HTTP(
            """<b style="color: red; font-size: 60px"> atilalimade@gmail.com </b>"""
        )
    else:
        return HttpResponseForbidden("Browser não suporta HTML.")
