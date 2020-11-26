from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm


def login_view(request):
    error_message=None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('fund')

            else:
                error_message=' wrong inserting'
    return render(request,'login.html',{'form':form,'error_message':error_message})




def logout_func(request):
    logout(request)

    return HttpResponseRedirect('/')





def signup_form(request):
    error_message = None
    add_message= None

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            add_message= 'Your account has been created!'
            return HttpResponseRedirect('/')
        else:
            error_message='wrong insert try again'
            return HttpResponseRedirect('/signup')


    form = SignUpForm()

    context = {
               'form': form,
               'add_message':add_message,
                'error_message':error_message,

               }
    return render(request, 'signup.html', context)