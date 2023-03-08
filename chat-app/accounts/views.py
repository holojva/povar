from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import UserProfile
from subscribers.models import SubscribeModel
from chat.models import ChatModel# Create your views here.

def login_view(request, *args, **kwargs):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
        return redirect("/")
        
    return render(request, "accounts/login.html", context={"form": form})
def registration_view(request, *args, **kwargs):
    form = RegisterForm(data=request.POST or None)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data["email"]
            user = User.objects.create_user(username=username, password=password, email=email)
            profile = UserProfile(profile=user)
            profile.save()
            return redirect("/login/")
    return render(request, "accounts/reg.html", context={"form": form})

def logout_view(request):
    logout(request)
    return redirect("/")
@login_required(login_url='/login/')
def profile_view(request):
    qs = ChatModel.objects.filter(user=request.user)
    return render(request, "accounts/profile.html", context={"profile":request.user, "ppl": len(list(SubscribeModel.objects.filter(other_user=request.user))), "subslist":list(SubscribeModel.objects.filter(other_user=request.user)), "chat": ChatModel.objects.filter(user=request.user), "sub": SubscribeModel.objects.filter(self_user=request.user)})