from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ChatForm
from .models import ChatModel
from subscribers.models import SubscribeModel
from django.contrib.auth.models import User
from .heh import func
# Create your views here.
def index_view(request) :
    form = ChatForm(data=request.POST or None)
    hello = request.GET.get('filter', '')
    sub = request.GET.get('sub', '')
    print(hello)
    only_subs = SubscribeModel.objects.filter(self_user__id=request.user.id)
    try :
        if int(hello) > len(list(User.objects.all())) :
            msg = ChatModel.objects.all()
            if sub == "true":
                msg = msg.filter(user_id__in=[user.other_user.id for user in only_subs])
                return render(request, "index.html", context={"msg": msg.reverse(), "form":ChatForm, "subs":SubscribeModel.objects.filter(self_user=request.user)})

            return render(request, "index.html", context={"msg": ChatModel.objects.all().reverse(), "form":ChatForm, "subs":SubscribeModel.objects.filter(self_user=request.user)})
    except:
        pass
    if hello != "" :
        

        msg = ChatModel.objects.filter(user=User.objects.get(pk=hello, ))
        if sub == "true":
            msg = msg.filter(user_id__in=[user.other_user.id for user in only_subs])
            return render(request, "index.html", context={"msg": msg, "form":ChatForm, "subs":SubscribeModel.objects.filter(self_user=request.user)})
    else :
        msg = ChatModel.objects.all()
        if sub == "true":
            msg = msg.filter(user_id__in=[user.other_user.id for user in only_subs])
            return render(request, "index.html", context={"msg": msg.reverse(), "form":ChatForm, "subs":SubscribeModel.objects.filter(self_user=request.user)})
        return render(request, "index.html", context={"msg": msg.reverse(), "form":ChatForm, "subs":SubscribeModel.objects.filter(self_user=request.user)})
@login_required(login_url='/login/')
def send_view(request):
    if request.method == "POST":
        form = ChatForm(request.POST or None)
        if form.is_valid() :
            user = request.user
            text = form.cleaned_data["text"]
            model = ChatModel.objects.create(user=user, text=text)
    return redirect("/")
def god(gotit):
    func()
# def profile_view(request):
#     user = request.user
#     qs = ChatModel.objects.filter(user=user)
#     return render(request, "accounts/profile.html", {"profile": user, "chat_data": qs})

