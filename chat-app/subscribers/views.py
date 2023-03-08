from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import SubscribeModel
# Create your views here.
@login_required(login_url="/login/")
def subscribe_view(request, *args, **kwargs):
    if request.user != get_object_or_404(User, pk=kwargs["pk"]) and not SubscribeModel.objects.filter(other_user=get_object_or_404(User, pk=kwargs["pk"]), self_user=request.user).exists():
        s_model = SubscribeModel(self_user=request.user, other_user=get_object_or_404(User, pk=kwargs["pk"]))
        s_model.save()
    return redirect("/")
    
    