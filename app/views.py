from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ContactModel, PostModel,CommentModel  
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.



def homepage(request):
    posts = PostModel.objects.all().order_by('-id')
    return render(request,'app/homepage.html',{"posts":posts})


def single_post(request,id):
    post = PostModel.objects.get(id=id)
    comments = CommentModel.objects.filter(post=post).order_by("-id")
    context={
       "post" : post,
       "comments" : comments
    }
    return render(request, 'app/single_page.html', context)
    return HttpResponse("Single post with id : {}".format(id))

@login_required
@require_http_methods(["POST"])
def add_comment(request,post_id):
    post_obj = PostModel.objects.get(id=post_id)
    comment_obj = CommentModel(post=post_obj, owner=request.user, comment_body=request.POST["msg"])
    comment_obj.save()
    return HttpResponseRedirect(reverse("app:single_post", args=(post_id)))
    
@require_http_methods(["POST","GET"])    
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username or not password:
             return render(request,'app/login.html',{"msg":"Both Username and Password required to Login."})
        else:
             user = authenticate(username=username, password=password)
             if user:
                  login(request, user)
                  return HttpResponseRedirect(reverse("app:homepage"))
             else:
                return render(request,'app/login.html',{"msg":"Invalid Username and Password."})

    elif request.method == "GET":
        msg =  request.GET.get("msg")
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("app:homepage"))
        return render(request,'app/login.html',{"msg":msg})

@require_http_methods(["POST","GET"])
def signup(request):
     if request.method == "POST":
      username = request.POST.get("username")
      email = request.POST.get("email")
      password = request.POST.get("password")
      password_confirm = request.POST.get("password_confirm")
      if not username or not email or not password or not password_confirm:
          return render(request,'app/signup.html',{"msg":"All fields are require to Login."})
      elif password != password_confirm:
          return render(request,'app/signup.html',{"msg":"Password and Confirm Password is not matching."})
      elif User.objects.filter(username=username).exists():
          return render(request,'app/signup.html',{"msg":"Username already exists. Please use different Username."})
      elif User.objects.filter(email=email).exists():
          return render(request,'app/signup.html',{"msg":"Email already exists. Please use different Email."})
      else:
          user = User.objects.create_user(username, email, password)
          return HttpResponseRedirect(reverse("app:login_user") + "?msg=Registered Successfully. Please Login to Continue.")
     else:
        return render(request,'app/signup.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("app:login_user"))

def about_user(request):
    return render(request,'app/about.html')


@require_http_methods(["POST","GET"])
def contact_user(request):
    if request.method == "POST":
     name=request.POST["name"]
     email=request.POST["email"]
     number=request.POST["number"]
     message=request.POST["message"]
     obj = ContactModel.objects.create(name=name,email=email,number=number,message=message)
     obj.save()
     return HttpResponseRedirect(reverse("app:homepage"))
    else:
        return render(request,'app/contact.html',{})













