from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


# Create your views here.
def Register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'user/register.html',context)
