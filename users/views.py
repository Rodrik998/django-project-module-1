from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.method == "GET":
        return render (request, 'users/login.html')
