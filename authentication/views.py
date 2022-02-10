from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST.get('pass1',False)
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return render(request,"authentication/success.html")
        else:
            messages.error(request,"Invalid credentials")
            return render(request,"authentication/index.html")
    return render(request,"authentication/index.html")
def signout(request):
    logout(request)
    return redirect("home")