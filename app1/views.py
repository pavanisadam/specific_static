from django.shortcuts import render

# Create your views here.
def s_static(request):
    return render(request,'s_static.html')