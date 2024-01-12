from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def apply(request):
    return render(request,'apply.html')
def IOTform(request):
    return render(request,'IOTform.html')
def cyberform(request):
    return render(request,'cyberform.html')
def MHTform(request):
    return render(request,'MHTform.html')
def EHform(request):
    return render(request,'EHform.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def notification(request):
    return render(request,'notification.html')
def admin(request):
    return render(request,'admin.html')