from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import MyLoginForm

# Create your views here.

def home(request):
   # if request.method == "POST":
   #     form = MyLoginForm(request.POST)
   #     if form.is_valid():
   #         # process form data
   #         username = form.cleaned_data['username']
   #         password = form.cleaned_data['password']
   #         # authenticate the credentials
   #         user = authenticate(username=username, password=password)
   #         if user is not None:
   #             if user.is_active:
   #                 login(request, user)
   #                 return redirect('restapp:resthome')
   #         else:
   #             form = MyLoginForm()
   #             context = {"message":"Welcome to API Home", "myform":form}
   #             return render(request, 'home/indexhome.html', context)

   # else:
   #     form = MyLoginForm()
    context = {'message': "Welcome to API Home"}
    return render(request, 'home/indexhome.html', context)


