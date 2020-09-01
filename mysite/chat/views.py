from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import Userregisterform
# Create your views here.
def home(request):
    return render(request,'chat/layout.html')
def register(request):
    if request.method=="POST":
        form=Userregisterform(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('login')
    else:
        form=Userregisterform()
    return render(request,'chat/register.html',{'form':form})
@login_required
def index(request):
    return render(request,'chat/index.html')
@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name})