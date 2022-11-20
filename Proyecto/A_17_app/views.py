from django.shortcuts import render, redirect
from .models import Auto
from .forms import AutoForm, NewRegister
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def subirauto(request):
    if request.method=="POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('dashboard')
    else:
        form=AutoForm()
    return render(request, 'subirauto.html',{'form':form})

def verautos(request):
    autos = Auto.objects.all()
    return render(request, 'verautos.html', {'autos': autos})

def revisarautos(request,pk):
    auto =Auto.objects.get(pk=pk)
    return render(request, 'revisarautos.html', {'auto':auto})

def borrarauto(request, pk):
    if request.method == "POST":
        auto = Auto.objects.get(pk=pk)
        auto.delete()
    return redirect('verautos')

def indexView(request):
    return render(request,'index.html')

def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            form = NewRegister()
    return render(request,'registration/register.html',{'form':NewRegister})