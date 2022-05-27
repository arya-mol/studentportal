from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView,TemplateView
from student.forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


class SignupView(View):
    def get(self,request):
        form=UserRegistrationForm()
        context={"form":form}
        return render(request,"signup.html",context)
    def post(self,request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User created")
            return render(request,"signup.html")
        else:
            context = {"form":form}
            return render(request,"signup.html", context)


class SigninView(View):
    def get(self,req):
        form=LoginForm()
        context={"form":form}
        return render(req,"signin.html",context)
    def post(self,req):
        form=LoginForm(req.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(req,username=username,password=password)
            if user:
                login(req,user)
                if req.user.is_superuser:
                    return redirect('signin')
                else:
                    return redirect("signin")
            else:
                context = {"form": form}
                return render(req, "signin.html", context)
def sign_out(request):
    logout(request)
    return redirect("signin")