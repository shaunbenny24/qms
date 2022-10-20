from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm,SignUpForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def privacy(request):
    return render(request, 'privacy.html')
def signin(request):
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         username = cd['username']
    #         password = cd['password']
    #         user = authenticate(request,username=username,password=password)
    #         if user is not None:
    #             print(user)
    #             print(password)
    #             login(request,user)
    #             #   return HttpResponse('You signed up succesfully!')
    #             return render(request,'index.html')
    #         else:
    #             pass


    form = LoginForm()
    return render(request, 'signin.html',{'form':form})
def signup(request):
    sign = SignUpForm()
    return render(request, 'signup.html',{'sign':sign})