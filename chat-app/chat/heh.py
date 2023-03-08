from django.contrib.auth.models import User
from .models import ChatModel
def func() :
    for i in range(1000):
        hello = User.objects.create(username=str(i), password="hahahaloser")
        wata = ChatModel.objects.create(user=hello, text="im dumb")